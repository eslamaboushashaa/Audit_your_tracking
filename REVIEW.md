# Skill and Prompt Review

Review date: 2026-10-11. Scope: the previous Audit_your_tracking package compared with the user's requests in this conversation. Output language: English. Platform: Meta only.

## Verdict

The previous version was a useful foundation, but it was not the strongest version for cross-platform use or precise audit conclusions. Version 2 fixes identifiable gaps and provides a portable skill bundle plus a self-contained prompt. It is structurally validated, not proven "best" across models or client environments.

No client website audit, Meta account access, test purchase, Claude installation, or live model comparison was performed during this package review.

## Findings and changes

| Previous issue | Change | Why it matters |
|---|---|---|
| README described a Codex skill and gave an invocation without installation/discovery instructions | Added distinct ChatGPT, Codex, Claude, and Claude Code usage; portable ZIP; explicit manual-reading fallback | A source folder is not automatically installed |
| Skill and large prompt were maintained independently | Canonical skill/references now generate the prompt and ZIP | Prevents conflicting instructions and stale copies inside this package |
| Prompt always asked for URL even when already supplied | Ask only when missing | Avoids unnecessary client friction |
| Short skill omitted detail present in full prompt | Added journey/capture reference and full account setup/fallback logic | Both entry points use the same workflow |
| EMQ target changed "above 8.5" into "at least 8.5" | Restored strict > 8.5 and distinguished client target from Meta requirements | Exactly 8.5 no longer incorrectly passes |
| Approval wording could appear to allow unavailable EMQ if disclosed | Missing mandatory evidence prevents overall PASS | Disclosure alone is not verification |
| Deduplication/overlap definitions and sample limits were ambiguous | Separated source delivery, key coverage, overlap, suppression, and population-level proof | A small passing sample or healthy UI label cannot prove global 100% |
| Coverage denominator could exclude actions with a missing source | Denominator includes all intended dual-source sample actions | Prevents a misleading 100% from incomplete delivery |
| Reconciliation lacked zero-denominator and multi-currency rules | Added undefined ratios, per-currency comparison, raw/adjusted totals, and recognition timing | Prevents invalid percentages and incomparable revenue |
| Server event counts could be mistaken for order coverage | Require matching distinct eligible order identities | Equal totals can hide duplicate and missing orders |
| Browser and CAPI types were too easily generalized | Separate route schemas; require current sources and original-type evidence | Avoids false failures from transport encoding or accepted API representations |
| Feature/server absence lacked NOT APPLICABLE | Added applicability rules distinct from missing access | Absence and uncertainty are different |
| Confirmation reload guidance lacked an explicit resubmission boundary | Only safe confirmation views; do not resubmit a POST | Avoids unintended extra orders |
| Original two-document outcome was not fully represented in the compact skill | Require audit report plus method/LLM handoff | Preserves reusable audit knowledge without exposing client data |
| Browser coverage and evidence handling needed more detail | Added consent/direct-click context, cross-domain checks, failed actions, HAR sanitation, and stable aliases | Expands visibility while keeping conclusions bounded |

## User-requirement mapping

| User requirement | Implemented location |
|---|---|
| English; Meta only | SKILL.md and README |
| Ask website URL first | SKILL.md: Start and adapt to the host |
| MCP before Chrome automation | account-access-and-evidence.md: Access sequence |
| Attempt trusted MCP setup if absent | Access sequence step 2 |
| Exact website Pixel ID equals selected Dataset ID | account-access-and-evidence.md: Dataset matching |
| Events Manager configuration, Browser/Server counts, signals, EMQ, diagnostics, CAPI | Capability and metric ledger |
| Correct trigger and real request | journey-and-capture.md; event trigger table |
| Required data and parameter types | meta-event-contract.md: Parameter and type validation; CAPI |
| More than one product in checkout and quantity >1 | Journey J05-J07; arithmetic fixture |
| Yesterday's real sales compared to Events Manager | meta-event-contract.md: Yesterday's sales reconciliation |
| Server EMQ above 8.5 | SKILL.md and contract EMQ section |
| Deduplication target 100% | Contract Deduplication section, with explicit proof boundaries |
| Detailed result and reusable methodology | report-template.md: Documents 1 and 2 |
| ChatGPT and Claude usability | README; portable SKILL.md; generated prompt and ZIP |

## Compatibility basis

The skill uses the shared folder/SKILL.md model with simple name/description metadata, relative references, and host-neutral instructions. It does not require Codex-specific tool names, a Claude-only command, or hard-coded MCP dependencies. The optional agents/openai.yaml remains OpenAI UI metadata.

Setup guidance was checked against official [OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills), [Claude Code documentation](https://code.claude.com/docs/en/skills), and [Claude custom skill help](https://support.claude.com/en/articles/12512180-use-skills-in-claude). This supports packaging and setup guidance; it does not establish that every host exposes browser/account tools.

Current Meta reference pages returned access errors during this review, and official-domain search did not recover their contents. The package therefore treats the field tables as working checklists and explicitly requires current official contract verification during each audit. This review does not certify every field's latest Meta requirement. Observed business logic can still be assessed independently of an inaccessible schema.

## Verification performed

- Read the previous skill, references, and standalone prompt against the conversation requirements.
- Reviewed revised instructions against the synthetic edge cases in validation/scenarios.md.
- Ran the installed skill-creator structural validator: valid skill.
- Built the standalone prompt from SKILL.md and all four references.
- Built a ZIP with one top-level meta-tracking-audit folder and the complete skill resources.
- Checked generated artifacts against canonical source bytes, local reference links, and ZIP integrity.

These are content/structure checks. The scenario file is an evaluation specification, not a claim that 33 model tests passed. Live execution in ChatGPT and Claude remains NOT RUN. Actual results will depend on tool access, account authorization, stock, checkout behavior, and available Meta evidence.

## Maintenance

Edit canonical files under skills/meta-tracking-audit and run tools/build_package.py, then tools/build_package.py --check. Do not hand-edit the generated prompt or ZIP. Keep the legacy prompt outside this package separate; it is not synchronized.

After a live evaluation, record product/model, tools, fixture, output, and failure evidence in the scenario log. Use observed failures to improve the shared source and rebuild both artifacts.
