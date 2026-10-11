# Account Access and Evidence

## Contents
- Access sequence
- Dataset matching
- Capability and metric ledger
- Evidence boundaries
- Evidence handling

## Access sequence

1. Discover authorized Meta MCP/connector operations first. Record exact tool names, authorization state, Business/account scope, and read capabilities. Do not infer Events Manager capability from an Ads connector name.
2. If absent, inspect the host's trusted connector/plugin catalog. When supported, set up an official or trusted integration through the host's normal installation and OAuth process, respecting required approvals. Never invent an MCP endpoint or install an unverified package. If setup is unavailable or remains blocked, continue.
3. Use MCP for supported account measurements. For missing, failed, unsupported, or ambiguous measurements, use authorized Chrome/browser automation at https://eventsmanager.facebook.com/events_manager2/list/dataset. Ask the user to sign in through Meta's interface if needed. Never request passwords, access tokens, recovery codes, two-factor codes, or session cookies.
4. If neither route provides a measurement, use a reliable Dataset export or contextual screenshot supplied by the client. Record its date, source, filters, and limits; a screenshot is not an order-level export.
5. With no route, continue website/Network inspection and mark each unavailable account metric NOT VERIFIABLE. With no browser/Network tools either, request sanitized HAR/request details and label the work an evidence review.

This priority applies to account measurements. Browser automation can be used immediately to test the website and identify its Pixel. Using Chrome through a DevTools MCP is browser tooling, not Meta account MCP access.

Keep account work read-only: do not change configuration, permissions, integration settings, diagnostics, or generate synthetic production events. Existing Test Events can be inspected. Any isolated test-environment setup needs appropriate authorization.

## Dataset matching

Derive the complete ID from a real collector request, corroborated runtime initialization, or other reliable website evidence. Preserve the ID as a string. An unexecuted source configuration alone establishes only a candidate ID.

Compare the website ID with the full Dataset ID before querying metrics or opening detailed diagnostics. Listing IDs/names to locate the matching Dataset is allowed; inspecting unrelated metrics is not. For website ID 1234, inspect only Dataset 1234; ignore Dataset 5678.

If multiple IDs receive events, record each and ask which are intended. Continue website evidence collection while waiting; do not combine results. If the supplied intended ID differs from the live destination, report the mismatch and resolve scope before inspecting either account's metrics. Never substitute a similar Dataset name.

Capture evidence of both IDs. A missing matching Dataset is an access/ownership gap, not proof of absent tracking.

## Capability and metric ledger

For every metric record:

| Measurement | MCP capability/result | Fallback reason | Final source/tool | Dataset | Event | Period/time zone | Filters/source | Extracted at | Evidence/status |
|---|---|---|---|---|---|---|---|---|---|

Cover Dataset configuration/connected assets, Browser and Server counts, last received time, EMQ, customer-information signals and coverage, deduplication diagnostics, warnings/rejected events, CAPI/partner status, and sample/Test Events details when exposed.

Use the UI/API's exact metric label, definition, denominator, rounding, reporting window, and processing delay. If unavailable, mark it unknown. Never rename "overlap" as "deduplicated percentage." Do not sum per-source counts and call the result unique purchases.

Use MCP as the primary source when supported. Cross-check through UI only for a stated need; investigate differences in filters, period, definitions, or freshness rather than selecting the convenient figure.

For unavailable account data, adapt this wording to the actual situation:

> No authorized route provided the required measurements for the website's matching Dataset during this audit. [List the unavailable metrics and whether MCP, browser access, or exports were unavailable or insufficient.] Website findings are based on the evidence listed and do not establish final Meta-side processing or account-wide Conversions API quality.

If no MCP exists but UI works, explicitly say "Meta MCP unavailable; Events Manager browser access used" and report the metrics obtained. Never imply every metric is missing solely because MCP is missing.

## Evidence boundaries

Do not treat these as interchangeable:

- Runtime action and request: what this browser actually sent.
- First-party response: that endpoint's result, not necessarily downstream Meta acceptance.
- CAPI request plus Meta response: API submission/receipt details; inspect errors, events_received, messages, and trace information when exposed. Batch acceptance without per-event detail limits individual conclusions.
- Events Manager sample: specific event/source receipt, subject to sample context.
- Aggregate account metrics: scoped reporting, not a proof of every order's identity.
- Source inspection: implementation intent; mark SOURCE-ONLY until executed.

An HTTP 200, pixel-helper badge, healthy connection label, or code snippet alone does not prove correct values, matching, deduplication, attribution, or unique counted purchases.

## Evidence handling

Assign stable IDs such as E001 to observations. Keep timestamps/time zone, action, test case, page/context, URL, request identifier, method, status, response, and artifact locator. Note capture loss, truncation, cache/service-worker effects, and navigation boundaries. Never reconstruct missing payload fields from guesses.

Capture raw and decoded representations separately in restricted local evidence only as necessary. Sanitize before sharing: HARs can include cookies, authorization, request bodies, PII, and session data. Do not commit raw HARs or credentials to the repository.

Use consistent aliases for customer-linked order/event IDs in reports, preserving equality relationships for deduplication. Dataset IDs and nonpersonal product IDs can remain for scope verification. Never expose raw contact details, delivery addresses, matching hashes, cookies, or tokens. Keep the authorized order reference privately available to its cancellation owner.

Validate PII normalization/hashing locally with authorized test inputs; never send customer information to a public hash site. Report presence, type, format, and equality outcomes instead of the values.
