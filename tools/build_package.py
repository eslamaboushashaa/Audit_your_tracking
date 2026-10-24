"""Build standalone prompts and portable skill ZIPs for three tracking platforms."""
import argparse
import io
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = {
    "meta": ("Meta Pixel and Conversions API Audit", "meta_pixel_capi_audit_master_prompt.md"),
    "tiktok": ("TikTok Pixel and Events API Audit", "tiktok_pixel_events_api_audit_master_prompt.md"),
    "snapchat": ("Snapchat Pixel and Conversions API Audit", "snapchat_pixel_capi_audit_master_prompt.md"),
}


def reference_names(platform):
    return (
        "account-access-and-evidence.md",
        "journey-and-capture.md",
        f"{platform}-event-contract.md",
        "report-template.md",
    )


def read(path):
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def sources(SKILL, REFERENCES):
    manifest = read(SKILL / "SKILL.md")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", manifest, re.S)
    if not match:
        raise ValueError("SKILL.md needs real YAML front matter and line breaks")
    # Deliberately restricted to this package's two single-line plain fields.
    fields = dict(line.split(": ", 1) for line in match[1].splitlines())
    if set(fields) != {"name", "description"}:
        raise ValueError("Portable manifest must contain name and description only")
    if fields["name"] != SKILL.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields["name"]):
        raise ValueError("Skill name must match its folder")
    if not 1 <= len(fields["description"]) <= 1024:
        raise ValueError("Invalid description length")
    if len(manifest.splitlines()) > 500:
        raise ValueError("Keep SKILL.md concise; move detail into references")
    refs = {name: read(SKILL / "references" / name) for name in REFERENCES}
    for name, body in {"SKILL.md": manifest, **refs}.items():
        if "\ufffd" in body or "\x00" in body:
            raise ValueError(f"Invalid text in {name}")
        if body.count("~~~") % 2 or body.count("```") % 2:
            raise ValueError(f"Unbalanced code fences in {name}")
    for target in re.findall(r"\]\((references/[^)]+)\)", manifest):
        resolved = (SKILL / target).resolve()
        if not resolved.is_relative_to(SKILL.resolve()) or not resolved.is_file():
            raise ValueError(f"Missing or unsafe reference: {target}")
        if resolved.name not in refs:
            raise ValueError(f"Reference not embedded in prompt: {target}")
    for name in REFERENCES:
        if f"(references/{name})" not in manifest:
            raise ValueError(f"Unlinked reference: {name}")
    return match[2].strip(), refs


def build_prompt(title, body, refs):
    for name in refs:
        body = body.replace(f"(references/{name})", f"(#reference-{Path(name).stem})")
    header = (
        f"# Master Prompt: {title}\n\n"
        "Use this complete workflow in ChatGPT, Claude, or another capable agent. "
        "It contains all required reference sections; no local skill files are needed. "
        "Discover actual tools and permissions before making capability claims.\n\n"
        "Generated from the canonical skill and references. Do not edit this copy directly.\n\n"
    )
    sections = [header + body]
    for name, text in refs.items():
        sections.append(f"## Reference: {Path(name).stem}\n\n{text.strip()}")
    sections.append(
        "## Begin the audit\n\n"
        "If no website URL was supplied, ask only for it and wait. "
        "Otherwise start scope and tool discovery, then follow the workflow above."
    )
    return ("\n\n---\n\n".join(sections) + "\n").encode("utf-8")


def build_zip(SKILL, REFERENCES):
    paths = [SKILL / "SKILL.md", SKILL / "agents" / "openai.yaml"]
    paths += [SKILL / "references" / name for name in REFERENCES]
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(paths):
            # Fixed metadata makes rebuilds deterministic.
            name = (Path(SKILL.name) / path.relative_to(SKILL)).as_posix()
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, read(path).encode("utf-8"))
    data = output.getvalue()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity failed")
        names = archive.namelist()
        if names.count(f"{SKILL.name}/SKILL.md") != 1:
            raise ValueError("ZIP must have one skill manifest")
        if any(not name.startswith(f"{SKILL.name}/") or ".." in Path(name).parts for name in names):
            raise ValueError("ZIP contains invalid paths")
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check existing outputs without writing")
    parser.add_argument("--platform", choices=("all", *PLATFORMS), default="all")
    args = parser.parse_args()
    outputs = {}
    selected = PLATFORMS if args.platform == "all" else (args.platform,)
    for platform in selected:
        skill = ROOT / "skills" / f"{platform}-tracking-audit"
        references = reference_names(platform)
        title, filename = PLATFORMS[platform]
        body, refs = sources(skill, references)
        outputs[ROOT / "prompts" / filename] = build_prompt(title, body, refs)
        outputs[ROOT / "dist" / f"{skill.name}.zip"] = build_zip(skill, references)
    for path, data in outputs.items():
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                raise SystemExit(f"STALE OR MISSING: {path.relative_to(ROOT)}; rebuild first")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        print(f"{'CHECKED' if args.check else 'BUILT'} {path.relative_to(ROOT)} ({len(data)} bytes)")
    print("Structure, references, and generated artifacts checked. Model behavior is not tested.")


if __name__ == "__main__":
    main()
