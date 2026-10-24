# Audit Your Tracking

Three separate English audit skills and prompts for **Meta, TikTok, and Snapchat**, usable with capable ChatGPT/Codex and Claude environments. Version 3, expanded 2026-10-24.

Each workflow tests real business triggers, request destinations, parameter types and meaning, matching signals, server receipt, deduplication, multi-product checkout, and yesterday's sales reconciliation. Each produces a client audit report plus an audit-method/LLM handoff.

## Choose a platform

| Platform | Full standalone prompt | Skill entry point | Uploadable skill ZIP |
|---|---|---|---|
| Meta | [Meta prompt](prompts/meta_pixel_capi_audit_master_prompt.md) | [meta-tracking-audit](skills/meta-tracking-audit/SKILL.md) | [Meta ZIP](dist/meta-tracking-audit.zip) |
| TikTok | [TikTok prompt](prompts/tiktok_pixel_events_api_audit_master_prompt.md) | [tiktok-tracking-audit](skills/tiktok-tracking-audit/SKILL.md) | [TikTok ZIP](dist/tiktok-tracking-audit.zip) |
| Snapchat | [Snapchat prompt](prompts/snapchat_pixel_capi_audit_master_prompt.md) | [snapchat-tracking-audit](skills/snapchat-tracking-audit/SKILL.md) | [Snapchat ZIP](dist/snapchat-tracking-audit.zip) |

Each ZIP has one skill folder, its own references, and optional OpenAI UI metadata. Each prompt embeds its complete workflow and references. No skill requires installing another platform's skill.

## Use in ChatGPT or Claude

For a conversation, paste or attach the selected full prompt and say:

> Follow this audit workflow for my website: [URL].

If the URL is missing, the workflow asks for it first. Full execution needs actual browser/Network capabilities and authorized account access; plain chat with no tools can only review supplied evidence.

For native skill use:

| Environment | Setup and invocation |
|---|---|
| Claude with custom Skills enabled | Upload the selected ZIP through the custom skill upload option in Customize > Skills, enable it, and ask to use it by name. |
| Claude Code | Copy the complete selected folder into .claude/skills/ at the project root. Invoke /tiktok-tracking-audit, /snapchat-tracking-audit, or /meta-tracking-audit. |
| Codex local project | Copy the complete selected folder into .agents/skills/ at the project root. Select it or invoke $tiktok-tracking-audit, $snapchat-tracking-audit, or $meta-tracking-audit. |
| ChatGPT with the skill registered in Skills | Select it with @ or ask to use the registered skill. If unavailable, use its standalone prompt. |

The authoring folders under skills/ are not automatically registered in every host. Copy supporting references together with SKILL.md. agents/openai.yaml is optional OpenAI UI metadata; Claude does not depend on it. This repository does not install skills globally, register connectors, or publish a plugin.

An agent with repository-file access can also be instructed directly:

> Read skills/snapchat-tracking-audit/SKILL.md and its references, then follow that workflow for [URL].

Replace the skill folder for the desired platform. Product permissions, code-execution availability, and skill controls still apply; a ZIP attachment alone is not proof of registration.

See [OpenAI skill setup](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Claude custom skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) for host-specific setup. Recheck the current UI if it differs.

## Common audit requirements

- Use the platform's authorized MCP first for account data; use Chrome/browser automation for missing capabilities, then scoped exports.
- Match the complete live website Pixel/source ID with the exact account source; ignore unrelated IDs.
- Test quantity 1, quantity >1, and at least two distinct products together in checkout.
- Compare original types separately from wire serialization and business meaning.
- Place a test order only when authorized for that audit; record cancellation ownership.
- Compare yesterday's eligible store sales with comparable event-source measurements, not campaign-attributed conversions.
- Separate sampled deduplication-key coverage from account-wide suppression; define the 100% target population.
- Report missing access and unresolved schema conflicts without fabricating metrics or granting overall PASS.

Tools and permissions are discovered at runtime. Advertising MCPs may expose campaign/pixel metadata without event quality or deduplication diagnostics. Browser UI access alone does not guarantee Network access.

## Platform distinctions

| Platform | Server integration | Important distinctions |
|---|---|---|
| Meta | Conversions API | Browser eventID/server event_id; Meta-specific field and EMQ checks |
| TikTok | Events API | ttq/page handling; Purchase versus legacy event mappings; TikTok properties/contents and event_id |
| Snapchat | Conversions API | Browser price/item_ids versus v3 value/content_ids; client_dedup_id/event_id and documented purchase fallback |

The Meta client target remains strictly above 8.5/10. For the new platforms, inspect their native quality metric and scale first. Do not silently convert 8.5 into a percentage or treat Snapchat EQS as Meta EMQ. Use >8.5 only when the actual native score supports that ten-point target; otherwise obtain an appropriate target.

Platform schema references and source-access caveats live in each skill's event-contract reference. The [expansion review](PLATFORM_EXPANSION_REVIEW.md) records the new platform distinctions and validation limits.

## Maintain and validate

Edit the canonical skill/reference files, then run from the repository root:

~~~text
python tools/build_package.py
python tools/build_package.py --check
~~~

To build or check just one platform:

~~~text
python tools/build_package.py --platform tiktok
python tools/build_package.py --platform snapchat --check
~~~

The standard-library builder produces all three prompts and ZIPs deterministically, validates local reference paths and basic structure, and detects stale artifacts. Do not edit generated prompts or ZIPs directly.

- [Original Meta review](REVIEW.md)
- [Meta evaluation scenarios](validation/scenarios.md)
- [TikTok evaluation scenarios](validation/tiktok-scenarios.md)
- [Snapchat evaluation scenarios](validation/snapchat-scenarios.md)

Structural validation is not a live audit or a cross-model behavior test. Live evaluation in ChatGPT and Claude still requires controlled runs with authorized tools/accounts. These prompts cannot guarantee evidence that the environment does not provide.
