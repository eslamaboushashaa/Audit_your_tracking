# Deliverables and Acceptance Criteria

## Status definitions

| Status | Meaning |
|---|---|
| PASS | Sufficient direct evidence for this check within its stated scope |
| FAIL | Reproducible evidence of a defect or an unmet agreed target |
| PARTIAL | Mixed verified results or an incomplete mandatory audit |
| NOT OBSERVED | Not seen during the specified capture window; not proof of universal absence |
| SOURCE-ONLY | Code describes behavior that was not executed |
| BLOCKED | An external condition stopped an attempted test |
| NOT VERIFIABLE | Necessary tools, access, source contract, or evidence are unavailable |
| NOT APPLICABLE | Feature/route/population is confirmed outside applicability; reason required |

Keep evidence source separate from verdict. A field can be Type PASS / Semantic FAIL. A missing optional field can be NOT APPLICABLE without making the event fail.

Overall PASS requires all mandatory agreed checks to pass with evidence. Missing required evidence means PARTIAL, BLOCKED, or NOT VERIFIABLE as appropriate. Known failures remain visible even if other checks are blocked. A browser-only audit can receive a scoped browser verdict, but cannot imply overall CAPI/account approval.

## Document 1: Client audit report

Filename suggestion: meta_tracking_audit_report.md.

### Executive outcome

State website, tested period, exact Dataset, overall status, key findings, and business impact first. Summarize:

- Browser Pixel trigger, payload, type, value, and destination correctness.
- Purchase runtime verification and test-order status.
- CAPI downstream receipt and limits of processing evidence.
- EMQ per required Server event, target > 8.5/10.
- Sample key coverage and actual Meta deduplication measurement, target 100% for the defined population.
- Yesterday's count/revenue reconciliation and identity-level coverage.
- Top three to five priorities and the material blockers.

Do not claim inferred revenue loss or attribution impact as measured fact.

### Scope, tools, and access

| Item | Result/evidence |
|---|---|
| Website/tested URLs/platform | |
| Test time/time zone/browser/device/consent | |
| Intended ID and observed website IDs | |
| Exact matching account Dataset | |
| Tools actually used and purpose | |
| MCP availability/capabilities | |
| Browser fallback and reason per missing metric | |
| Export/screenshot context and limitations | |
| Test-order authorization/method/budget/cancellation owner | |
| Agreed value/recognition policy | |
| Untested or excluded scope | |

Include the capability ledger from the account-access reference. Explicitly distinguish Meta account MCP from Chrome DevTools/browser tooling. No MCP does not mean no account evidence if browser access worked.

### Architecture and evidence chain

Map action -> application state -> SDK/browser collector -> first-party/server integration -> Meta receipt/reporting. Mark unknown stages and implementation owners. Reference evidence for each proven link.

### Journey and event coverage

| Case/action | Expected Meta event/count | Actual semantic count | Browser/Server route | Trigger | Destination | Evidence | Status/blocker |
|---|---|---|---|---|---|---|---|

Include multi-product checkout, quantity >1, failed-action checks, and confirmation reload outcome. Mark feature absence with NOT APPLICABLE rather than silently dropping it.

### Event-specific parameter audit

One table per important event and route. Include all observed fields plus applicable required fields that are absent.

| Field/path | Sanitized raw/decoded value | Actual original type or unknown | Expected route type | Requirement and official source | Type verdict | Meaning verdict | Evidence |
|---|---|---|---|---|---|---|---|

Include serialization uncertainty, null/empty values, nested content objects, currency, and ID policy. Identify which current documentation could not be verified.

### Multi-product arithmetic

| Product/variant | Unit price | Quantity | Line discount | Expected line total | Observed contents | Evidence/result |
|---|---|---|---|---|---|---|

Show subtotal, total units, discounts, included tax, shipping, fees, rounding policy, stage-specific expected value, browser value, server value, final order value, and differences. Avoid adding already-included tax or subtracting discounts twice.

### CAPI, signals, EMQ, and diagnostics

| Event | Meta receipt evidence | EMQ/target | Signals and valid coverage | Period/denominators | Diagnostics/rejected counts | Source | Verdict |
|---|---|---|---|---|---|---|---|

Separate signal presence, formatting, hashing, coverage, and observed score. Preserve Meta's metric definitions. List unsupported or unavailable measurements individually.

### Deduplication

| Action alias | Event/Dataset | Browser ID alias | Server ID alias | Both sources? | Key match? | Meta outcome | Evidence |
|---|---|---|---|---|---|---|---|

Show tested population, numerator/denominator, sample key coverage, account metric's exact label/definition, period, and limits. Never rename overlap as suppression or claim account-wide 100% from a sample.

### Sales reconciliation

State the exact day/interval/time zone, event recognition policy, eligible order rules, exclusions, currency, extraction times, and reporting delay.

| Currency | Store eligible count/value | Comparable Meta count/value | Absolute differences | Ratios or undefined | Order-level match coverage | Verdict/evidence |
|---|---|---|---|---|---|---|

Separate raw totals from adjusted totals, and evidence-supported explanations from hypotheses. List missing, duplicate, extra, and mismatched orders under consistent aliases when possible.

### Findings and fixes

For every finding include title, P0-P3 priority, affected event/route, reproduction steps, expected behavior and source, actual behavior/types/values, evidence IDs, proven impact/limits, recommended fix, owner if known, and measurable acceptance test.

- P0: Severe Purchase corruption or exposed sensitive data requiring immediate attention.
- P1: Defect materially affecting revenue measurement, optimization, or deduplication.
- P2: Funnel or parameter-quality gap.
- P3: Lower-impact improvement.

Missing access is a limitation, not automatically a defect. Separate a client-target gap from a Meta contract violation.

### Retest, limitations, and evidence appendix

List exact outstanding tests and access needed. Include sanitized evidence IDs, artifact locators, timestamps, tool truncations, sources and access dates. Explicitly state any untested browser, consent, catalog, ad-click, or cross-domain behavior. No empty filler or invented screenshots.

## Document 2: Audit method and LLM handoff

Filename suggestion: meta_tracking_audit_method_and_handoff.md.

Include:

1. Scope and stop point; which steps were executed vs proposed.
2. Tool inventory, actual tool names, capability gaps, account access order, and exact Dataset matching method.
3. Reproducible journey steps, capture timing, observation windows, and safe order boundary.
4. Sanitized request decoding and how original types were established or remained unknown.
5. Arithmetic, EMQ interpretation, deduplication population, and sales-reconciliation definitions.
6. Evidence index and report cross-references.
7. Blockers, unsuccessful attempts, and specific information needed next.
8. Reusable lessons and traps, with illustrative examples clearly distinguished from client observations.
9. Follow-up acceptance tests, test-order cancellation status, and ownership.

Never include credentials, raw PII, hidden reasoning, or unredacted HARs. Describe the observable method and evidence-supported decisions, not private chain-of-thought. Do not claim a tool was used simply because the workflow recommends it.

## Final quality gate

Check all mandatory test cases are accounted for; all conclusions have evidence; all required parameter/type claims have a source or explicit uncertainty; sample/global metrics are separated; zero denominators and currencies are handled; no unrelated Dataset is included; and missing evidence cannot yield overall PASS.
