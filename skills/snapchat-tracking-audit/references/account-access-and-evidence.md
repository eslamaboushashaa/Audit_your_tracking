# Snapchat Account Access and Evidence

## Contents
- Access order and scope
- Source identity
- Measurement ledger
- Evidence boundaries and handling

## Access order and scope

1. Discover available Snapchat MCP/connector operations and authorization. Record actual tool names, account/organization scope, and capabilities.
2. If absent, inspect the host's trusted catalog and use supported official/trusted setup. Complete required OAuth/install approvals through the host; never request passwords, access tokens, session cookies, or two-factor codes in chat. If setup cannot be completed, continue with fallback.
3. Use MCP for supported account measurements. For unavailable, unsupported, failed, or ambiguous metrics, use an authorized Chrome session at [Snapchat Ads Manager](https://ads.snapchat.com/), then navigate the live UI to Snapchat Ads Manager > Events Manager > Event Sources. Do not hard-code account IDs, stale deep links, or screen coordinates.
4. If neither route works for a metric, request a reliable scoped export or contextual screenshot. Record its source, date, selected ID, period, time zone, filters, and limits.
5. Continue website/Network work when account evidence is absent. If browser tools cannot expose requests either, request sanitized request/HAR evidence and label the result an evidence review, not a completed live audit.

A Chrome DevTools MCP is browser tooling, not Snapchat account MCP access. Ad reporting tools do not automatically expose received-event counts, matching quality, or deduplication diagnostics.
The official Snap Ads MCP is read-only and can expose account/pixel resources. Inspect the operations actually offered; pixel metadata or campaign statistics alone do not establish CAPI receipt, EQS, or deduplication. Do not invent unsupported endpoints behind this connector.

Do not edit source settings, permissions, consent choices, warnings, integrations, or campaign optimization as part of an audit. Read existing test-event evidence when available; isolated validation submissions require authorization and must remain separate from production receipt proof.

## Source identity

Use real request/runtime evidence to establish the complete Pixel ID. Keep opaque IDs as strings; preserve characters, case, hyphens, and leading zeros. Confirm website destination, account source, and server destination refer to the same intended asset.

For a site using source A, inspect source A; skip source B even if its display name looks similar. Listing source IDs/names to find A is permitted; reading B's metrics is not. Record both sides of the identity match.

With multiple observed IDs, ask which are intended before account metrics are gathered or combined. An intended-versus-observed mismatch is a finding, not permission to substitute another account source. A source missing from the authorized account means an access/ownership gap. Source-code configuration without a dispatched event identifies a candidate, not a confirmed live destination.

Distinguish a web Pixel ID from a Snap App ID or ad account ID. Verify the web source against the CAPI endpoint's asset ID.

## Measurement ledger

| Measurement | MCP capability/result | Fallback reason | Actual source/tool | Asset ID | Event | Date range/time zone | Domain/connection filters | Extraction time | Evidence/status |
|---|---|---|---|---|---|---|---|---|---|

Cover:
- Source configuration, connected assets, domains, native/partner/gateway owner.
- Browser/Server received-event counts and latest receipt.
- Event Quality Score (EQS), its scale, scope, rounding, and measurement period.
- Distinct matching fields, valid presence, coverage and denominators.
- Deduplication identifiers, overlap, diagnostics and suppression metrics if exposed.
- Rejected events, malformed parameters, warnings and affected counts.
- Conversions API (CAPI) receipt/response evidence and relevant test/sample events.

Record exact UI/API labels. Unknown denominator, uniqueness, or reporting basis stays unknown. Never add Browser and Server counts to invent unique conversions. Use MCP first where supported; if sources disagree, investigate filters, time zones, definitions, and lag.

If MCP is absent but UI succeeds, state that browser access supplied the metric. If no route supplies it, use:

> No authorized route provided [specific measurements] for this website's matching Snapchat event source. [State MCP/browser/export availability accurately.] Website evidence does not establish platform-side processing or account-wide server tracking quality.

## Evidence boundaries and handling

Assign E001-style IDs with action/test case, URL, time zone, timestamp, page/context, request ID, initiator, method, payload, response/status, and artifact locator. Capture original and decoded payloads separately.

Separate browser dispatch, first-party enqueue, downstream submission, platform receipt, processing, deduplication, and reporting. An HTTP 200 or healthy connection badge proves none of the later stages by itself. For a server batch, correlate response-level and per-event errors rather than assuming every event was accepted.

A source snippet is SOURCE-ONLY until executed. A UI screenshot cannot establish hidden request types. Document truncation, lost navigation requests, failed capture, observation windows, and any passive instrumentation; do not fill gaps with assumptions.

Keep raw evidence restricted and only as needed. HARs and CAPI URLs can contain credentials and PII. Redact before sharing or committing. Use stable aliases for customer-linked event/order identifiers to preserve matching comparisons. Nonpersonal product IDs and the intended source ID may remain to establish scope.

Never expose email, phone, address, customer hashes, click/cookie identifiers, auth headers, access tokens, or session cookies in deliverables. Validate normalization/hashing locally using authorized inputs, never a public hashing website. Give the authorized test order's cancellation reference privately to its owner.
