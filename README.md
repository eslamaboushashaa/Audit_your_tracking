# Audit Your Tracking

English, Meta-only tracking audit package for ChatGPT/Codex and Claude. Version 2, reviewed 2026-10-11.

The workflow preserves Meta MCP first, Chrome Events Manager fallback, exact Dataset matching, parameter/type checks, multi-product checkout, EMQ > 8.5, a precisely defined 100% deduplication target, and yesterday's sales reconciliation.

## Choose your entry point

| Environment | Use |
|---|---|
| ChatGPT or Claude conversation | Paste or attach the full [standalone prompt](prompts/meta_pixel_capi_audit_master_prompt.md), then say: "Follow this audit workflow. My website is [URL]." |
| Claude with custom Skills enabled | Upload [meta-tracking-audit.zip](dist/meta-tracking-audit.zip) in Customize > Skills using the skill upload option; enable it, then request the audit by name. |
| Claude Code | Copy the complete [skill folder](skills/meta-tracking-audit/) to your project's .claude/skills/meta-tracking-audit/. Invoke /meta-tracking-audit or ask to use it. |
| Codex local project | Copy the complete skill folder to your project's .agents/skills/meta-tracking-audit/. Select the skill or invoke $meta-tracking-audit. |
| ChatGPT with the skill registered in its Skills interface | Select the registered skill using @ or ask to use it by name. If it is not registered, use the standalone prompt. |

The source folder under Audit_your_tracking/skills is an authoring location; it is not automatically registered in every product. This update does not install globally or publish a plugin. Copy the references with SKILL.md; agents/openai.yaml is optional OpenAI UI metadata, not a Claude dependency.

For an agent that can read this repository, no installation is needed to explicitly request:

> Read skills/meta-tracking-audit/SKILL.md and its referenced files from this package's root, then follow that workflow to audit [URL].

Claude upload requires its supported skills/code-execution capability and applicable workspace permissions. ChatGPT product surfaces differ: a ZIP attachment is not automatically a registered skill. The standalone prompt is the fallback for either product.

Installation details follow [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills), [Claude Code skill documentation](https://code.claude.com/docs/en/skills), and [Claude custom skill instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Recheck these sources if the product UI changes.

## Tools and access still matter

Neither a prompt nor a skill grants access to Meta, Chrome, Network logs, or customer systems. The agent must discover the tools actually available.

A complete audit typically needs website browser/Network inspection, authorized matching Dataset access, sales figures/export, and permission for one test order. Use Meta MCP first; if absent or insufficient, use Chrome/browser automation for missing account measurements. Trusted connector setup is conditional on host support and official authorization.

Without those capabilities, the workflow produces an explicitly limited evidence review and asks for the missing evidence. It must never claim a full live audit, EMQ, CAPI receipt, or account-wide deduplication from a generic chat alone.

## Included files

- [SKILL.md](skills/meta-tracking-audit/SKILL.md): concise portable workflow.
- [References](skills/meta-tracking-audit/references/): access/evidence, journey/capture, event contracts/calculations, and two deliverable templates.
- [Standalone prompt](prompts/meta_pixel_capi_audit_master_prompt.md): full workflow and references in one copyable file.
- [Skill ZIP](dist/meta-tracking-audit.zip): one top-level skill folder with its resources.
- [Review](REVIEW.md): previous gaps, changes, requirement mapping, and validation limits.
- [Evaluation scenarios](validation/scenarios.md): cases for testing real model behavior.

## Maintain one source

Edit SKILL.md and the reference files, then rebuild the prompt and ZIP from the package/repository root:

~~~text
python tools/build_package.py
python tools/build_package.py --check
~~~

The builder uses only Python's standard library, checks local reference paths and basic structure, and compares generated artifacts byte-for-byte in check mode. It is not a Meta payload validator or an LLM behavior test. No dependencies, account access, installation, or network calls are performed.

The prompt inside this repository is canonical. Any older copies outside this package are legacy drafts and are not maintained by this build.

## Validation boundary

The instructions and package can be structurally checked here. End-to-end execution inside both ChatGPT and Claude still requires separate runs with their available tools and authorized accounts. No prompt can guarantee an accurate audit regardless of access or evidence.
