# Snapchat Deliverables and Acceptance Criteria

## Status definitions

| Status | Meaning |
|---|---|
| PASS | Sufficient evidence verifies this specific check and scope |
| FAIL | Reproducible defect or confirmed unmet agreed target |
| PARTIAL | Mixed verified results or incomplete required scope |
| NOT OBSERVED | Absent during the stated observation window; not proof of universal absence |
| SOURCE-ONLY | Seen in code without execution in the real journey |
| BLOCKED | External condition stopped an attempted test |
| NOT VERIFIABLE | Necessary tools, source contract, access, or evidence unavailable |
| NOT APPLICABLE | Confirmed outside feature/route/population applicability, with reason |

Separate evidence source from verdict. A field may be Type PASS / Semantic FAIL. Missing optional fields do not automatically fail events. A critical defect remains visible even if other checks are blocked.

Overall PASS requires all mandatory agreed tests to pass with sufficient evidence. Missing required Purchase, original type, server receipt, account quality, deduplication or reconciliation evidence prevents overall PASS. A scoped browser-only verdict must not imply Conversions API (CAPI) or account-wide approval.

## Document 1: Snapchat audit report

Suggested filename: snapchat_tracking_audit_report.md.

### Executive result

Lead with website, exact Pixel ID, dates, tested environment, overall status, top priorities and measured business impact. Distinguish proven consequences from risks.

Summarize browser trigger/destination/types/meaning, completed-order proof, server receipt, native Event Quality Score (EQS) and applicable target, dedup sample versus account outcome, yesterday's count/revenue comparison, and open blockers.

### Scope, access, and architecture

| Item | Result and evidence |
|---|---|
| Website, URLs, platform, browser/device | |
| Start/end time, time zone, consent/login state | |
| Intended and observed source IDs | |
| Exact account source match | |
| API/SDK/integration versions and owner | |
| Actual tools used and capabilities | |
| MCP result, browser fallback reason, exports | |
| Value/recognition policy and currencies | |
| Test-order authorization/budget/method/cancellation owner | |
| Excluded or untested scope | |

Include the per-metric access ledger from the access reference. Draw or describe action -> app state -> browser SDK/collector -> gateway/server -> platform response -> account reporting; link evidence for every established stage. Mark unknown stages.

### Journey/event matrix

| Case/action | Expected event/count | Observed event/logical count | Browser/server | Trigger | Destination | Evidence | Status/blocker |
|---|---|---|---|---|---|---|---|

Cover quantity 1, quantity >1, two products in the same checkout, safe failed actions, accepted payment state, successful order, and safe revisit. Record exact event-code/version mapping, particularly legacy or partner aliases. Do not count metadata/transport as conversions.

### Parameter and type tables

Create a table for each important event and route, including missing applicable required fields:

| Field/path | Sanitized raw and decoded value | Actual original type or unknown | Expected route type | Requirement and official source | Type verdict | Semantic verdict | Evidence |
|---|---|---|---|---|---|---|---|

Include nested arrays/objects, quantities, product IDs/variants, timestamp unit, amount/currency, matching identifiers and dedup keys. Distinguish SDK input, gateway transformation, and final API JSON. Cite any unresolved source conflict and stop short of an unsupported type failure.

### Multi-product calculation

| Product/variant | Unit amount | Quantity | Discount | Expected line total | Browser/server representation | Evidence/verdict |
|---|---|---|---|---|---|---|

Show subtotal, units, discounts, included tax, shipping, fees, rounding and approved stage-specific total. Compare every available layer and report where product B, quantities, or prices diverge. Do not require unsupported item fields in an unrelated SDK.

### Server, matching, quality, and diagnostics

| Event/source | Receipt evidence | Quality label/value/scale | Signals and valid coverage | Period/denominators | Warnings/errors | Target applicability | Verdict |
|---|---|---|---|---|---|---|---|

Record native Event Quality Score (EQS); do not infer score or scale from another platform. Keep signal count, valid coverage, catalog match rate, and event match quality separate. A >8.5/10 target applies only on a verified compatible scale; otherwise request a native target.

### Deduplication

| Action alias | Event/source | Browser key alias | Server key alias | Expected sources received? | Key agreement | Alternative mechanism if supported | Platform outcome | Evidence |
|---|---|---|---|---|---|---|---|---|

Give sample numerator/denominator and account metric's exact label, scope and definition. Show missing-source cases. No account-wide 100% from a passing sample, an overlap label, or no diagnostics.
For PURCHASE record client_dedup_id/event_id separately from transaction_id/custom_data.order_id. State which supported mechanism is evidenced and which remains unverified.

### Sales reconciliation

State date/time-zone interval, eligibility, recognition moment, currency, raw totals, adjustments, and processing delay before calculating.

| Currency | Store count/value | Comparable platform count/value | Absolute differences | Ratios or undefined | Identity-match coverage | Explained exclusions | Evidence/verdict |
|---|---|---|---|---|---|---|---|

Do not use attributed campaign conversions. Zero denominators stay undefined. Separate currencies, preserve ratios above 100%, and avoid claiming identity coverage from matching aggregates. List missing, duplicated, extra, late and value-mismatched orders under aliases when available.

### Findings and acceptance tests

Each finding needs:
1. P0-P3 priority and concise title.
2. Affected event/route/version.
3. Reproduction steps and actual business state.
4. Expected behavior with source or approved policy.
5. Actual fields, original types, values, and timestamps.
6. Evidence IDs and proven impact/limits.
7. Specific recommended correction and responsible owner if known.
8. Measurable retest/acceptance condition.

P0: severe revenue corruption or exposed sensitive data. P1: material revenue, deduplication, or optimization-data defect. P2: funnel/parameter quality gap. P3: lower-impact improvement. Access gaps are limitations, not automatically implementation defects. Separate client quality targets from platform acceptance requirements.

### Retest, limitations, and evidence index

Account for every required untested case, native score/metric unavailable, unresolved schema conflict, consent/browser/device/cross-domain scope, catalog dependency, capture truncation, and pending cancellation. Include sanitized artifacts, observation times, source URLs and access dates. Do not invent screenshots, receipt logs, test results, or current source verification.

## Document 2: Method and LLM handoff

Suggested filename: snapchat_tracking_audit_method_and_handoff.md.

Include:
- Executed scope and exact stopping point versus proposed next steps.
- Actual tools, capability gaps, MCP-first route, and ID matching method.
- Reproducible journey/capture sequence and safe order boundary.
- Request decoding and how original types were established or stayed unknown.
- Platform-specific event/schema/version distinctions encountered.
- Calculations, quality scale, dedup population/mechanism, reconciliation definitions.
- Sanitized evidence index and client-report references.
- Blockers, failed attempts, remaining inputs and acceptance tests.
- Reusable lessons, with synthetic examples clearly labeled.
- Test-order cancellation owner/status.

Explain observable procedures and evidence-supported decisions, not hidden chain-of-thought. Do not include customer PII/hashes, credentials, raw HARs, or claims of tool use unsupported by the execution log.

## Final check

Every required test is covered or explicitly blocked; all conclusions have evidence; types and meaning are separate; current contract uncertainty is visible; native metric definitions and sample/global boundaries are preserved; ratios have meaningful denominators; currencies are separate; no unrelated source or secrets appear. Missing evidence cannot yield overall PASS.
