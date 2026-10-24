# Snapchat Event Contract and Calculations

## Contents
- Sources and version selection
- Browser Pixel
- CAPI v3
- Matching and receipt
- Deduplication mechanisms
- Quality and reconciliation

## Sources and version selection

Reference review: 2026-10-24. Reopen relevant official documentation at audit time and record URL, access/update date, observed version, requirement, type, and source evidence. This workflow audits website events; app-only fields are not automatically required.

- [Direct Pixel implementation](https://businesshelp.snapchat.com/s/article/pixel-direct-implementation?language=en_US)
- [Official Snap GTM template](https://github.com/Snapchat/snapchat-google-tag-manager/blob/main/template.tpl)
- [Pixel installation guidance](https://businesshelp.snapchat.com/s/article/pixel-website-install?language=en_US)
- [Pixel/catalog requirements](https://businesshelp.snapchat.com/s/article/pixel-dynamic-best?language=en_US)
- [CAPI parameters](https://developers.snap.com/marketing-api/Conversions-API/Parameters)
- [Using CAPI](https://developers.snap.com/marketing-api/Conversions-API/UsingTheAPI)
- [v2 to v3 migration](https://developers.snap.com/marketing-api/Conversions-API/MigrationGuide)
- [Deduplication](https://developers.snap.com/marketing-api/Conversions-API/Deduplication)
- [Validation and test receipt](https://developers.snap.com/marketing-api/Conversions-API/VerifySetUp)
- [Events Manager Pixel details](https://businesshelp.snapchat.com/s/article/events-manager-pixel-details?language=en_US)
- [Official Ads MCP](https://developers.snap.com/marketing-api/Ads-MCP/Introduction)

CAPI pages and the official template were readable during preparation. Some Business Help pages rendered CSS errors; indexed official material supplied context, not a complete browser type schema. The CAPI parameter table and examples contain type/casing inconsistencies. Resolve discrepancies with the current route's schema, installed SDK, authorized validation, and documented response; report uncertainty rather than asserting an unsupported failure.

Determine browser SDK, partner/gateway transformation, CAPI version and web asset before comparing. Browser fields, legacy CAPI v2, and CAPI v3 have different contracts.

## Browser Pixel

Map real actions to actual supported names:

| Action | Snap browser event |
|---|---|
| Logical page navigation | PAGE_VIEW |
| Product detail | VIEW_CONTENT |
| Search submitted | SEARCH |
| Successful cart addition | ADD_CART |
| Checkout entry | START_CHECKOUT |
| Accepted payment/billing state | ADD_BILLING |
| Successful purchase milestone | PURCHASE |
| Wishlist addition | ADD_TO_WISHLIST |
| Registration | SIGN_UP |

These names are represented in Snap's official template. Do not copy Meta's AddToCart or InitiateCheckout into Snap. SAVE is a distinct event; do not silently treat it as a universal wishlist alias.

Browser fields to inspect include price, currency, transaction_id, item_ids, item_category, number_items, search_string, and client_dedup_id. The template's form-control type TEXT is not a complete JavaScript SDK type specification. Inspect the resolved input, any conversion in the template, the installed SDK contract, and actual collector serialization.

| Browser field | Check to perform |
|---|---|
| price | Valid transaction/action amount; establish accepted number/numeric-string types from current browser contract |
| currency | Supported currency string corresponding to price |
| transaction_id | Stable order reference; preserve identity |
| item_ids | All relevant IDs in an accepted representation; establish element types and catalog mapping |
| item_category | Supported category representation; no automatic Meta rule |
| number_items | Correct total units; establish original type and supported coercion |
| search_string | Actual submitted query, without sensitive data |
| client_dedup_id | Explicit stable string key for cross-source matching |

Pixel installation guidance specifically calls out price, currency, and transaction_id for PURCHASE. Do not assume a browser value field replaces price because CAPI v3 uses value. Likewise, do not require CAPI's contents[] in a browser SDK that does not support that structure. Independently validate all cart lines and transformation coverage.

For quantity 2 at unit 7, the amount added is 14 under an added-value policy. For A 7 x 2 plus B 11 x 1, item subtotal is 25 and total units are 3. If the approved purchase value includes shipping 5, browser Purchase price should represent 30. It is not simply A's unit price.

Preserve raw and decoded collector fields. Internal aliases, compressed payloads, URL encoding, and SDK coercion are not themselves type defects. Trace data from real snaptr calls; source-only configuration or a similar first-party object does not establish dispatched original types. Report unknown types separately from verified semantic errors.

## CAPI v3

Use the observed API version. Current web v3 endpoint shape is https://tr.snapchat.com/v3/{PIXEL_ID}/events; credentials must never appear in report URLs. The JSON envelope contains data[], with event-level server fields and user_data/custom_data. Web action_source is WEB in the documented web example; do not import another platform's website literal without checking support.

Required web context and matching requirements must be checked against the current Using CAPI page, including event name/time/source/URL, user_data, and a supported match combination. PURCHASE requires currency and value. A browser or v2 price field does not substitute for v3 custom_data.value.

Compact v3 type checkpoints from the parameter reference:

| Path | Documented checkpoint |
|---|---|
| event_name | String |
| event_time | Integer; seconds or milliseconds supported |
| event_source_url | String URL |
| event_id | String |
| custom_data.value | Float |
| custom_data.currency | String |
| custom_data.num_items | String |
| custom_data.order_id | String |
| custom_data.content_ids | List of strings; check documented accepted forms |
| custom_data.content_category | String or list of strings |
| custom_data.contents | List of objects |

Snap's parameter page permits both timestamp granularities and recommends milliseconds; it also states a seven-day maximum age. Recheck current limits. Do not label milliseconds wrong merely because Meta uses seconds. Record the actual unit and action time.

The same documentation set contains examples using numeric strings, including value/quantity/item_price, despite table types; another example differs in event-name case. An example is not proof that all coercions are supported. Prefer an explicit current field schema and authorized validation outcome; if contradictory, document the conflict and keep the unsupported type conclusion provisional.

Inspect contents[].id, quantity, item_price and optional fields using the exact nested schema. Total units, item subtotals and final value must agree with the order regardless of accepted representation. Do not call v3 num_items as a string invalid by applying Meta's integer rule. Do not import a browser number_items requirement into v3.

Inspect v2 requests against their supported v2 schema before recommending migration. When a gateway converts v2/browser inputs to v3, audit both boundaries and actual transformed output. An old field name at the input is not proof of an invalid downstream payload.

## Matching and receipt

For v3 user_data inspect em/ph and other legitimately collected supported identifiers, client_ip_address/client_user_agent, sc_cookie1 and sc_click_id. _scid and landing-page ScCid are relevant source identifiers; verify actual mapping/persistence instead of copying Meta fbp/fbc. Use per-field scalar/list, normalization, and hashing rules.

Do not infer hash behavior from a generic "user data" label. Inspect SDK automatic hashing versus explicit prehashing, double hashing, proxy versus client network data, and valid nonempty values. Validate locally and redact values/hashes from reports. Do not fabricate a click ID on a direct visit.

Require a real downstream response and/or matched account event for CAPI receipt. Capture errors, per-event validity, batch boundaries and trace details; a first-party 200 or queued task is insufficient.

Snap supplies a separate /events/validate route and test logs. Use only when authorized with secure credentials, and label the results as test validation. A validated payload or test receipt does not prove that the production order pipeline delivered or counted the event. Do not replay a real purchase to the production endpoint just to validate schema.

## Deduplication mechanisms

Snap documents browser client_dedup_id paired with CAPI event_id, for the same Pixel and event name. The browser's automatically generated identifier is not automatically known to the server; confirm deliberate propagation or a supported integration mechanism.

Current documentation also supports a PURCHASE fallback: browser transaction_id paired with v3 custom_data.order_id. It describes 48 hours for the cross-channel key and up to 30 days for the purchase order-reference mechanism, with the shared-key pair taking precedence. Verify current conditions before judging.

Record both mechanisms independently. Do not import a blanket Meta assumption that order references can never deduplicate. A missing preferred key can be a coverage improvement while a valid documented purchase fallback suppresses duplicates. Conversely, equal order IDs alone do not establish the platform outcome without matching event/source/timing evidence.

Use unique real identifiers per conversion, stable across retries, never session-wide IDs or unresolved template placeholders. Avoid ID precision loss and whitespace/case changes. Retain exact comparisons privately and expose consistent aliases.

## Quality and signal coverage

Record the platform's exact metric name, native scale, event/source scope, window, filters, timestamp, rounding, and recommendations. Count distinct supported signals separately from valid per-event coverage. Empty, malformed, or improperly hashed fields do not count as valid coverage.

The client's ambition remains strictly above 8.5/10 where the native score is verifiably ten-point. Do not automatically convert that to 85%, map a categorical rating, average events to hide a weak purchase score, or use a different platform's score. If the native scale differs, request a suitable target; continue other work and mark target evaluation pending. An unavailable score is NOT VERIFIABLE, not zero. Confirmed absent server tracking can make server-only checks NOT APPLICABLE; a platform-wide score may still be available for browser traffic.

Use legitimately collected authorized signals; do not invent identifiers or collect additional sensitive data to inflate quality. High matching quality does not prove correct triggers or revenue.

## Deduplication measurement

Evaluate delivery, key agreement, and platform suppression separately. The target is 100% for a stated intentionally duplicated population, not 100% overlap across every event regardless of architecture.

~~~text
Sample shared-key coverage % =
  tested intended dual-source actions with both sources and valid matching keys
  / all tested intended dual-source actions * 100
~~~

Include actions missing an expected source in the denominator. For 2 matched of 3 intended actions, report 66.67%, not 100%. Keep documented alternative mechanisms in a separate column; a missing preferred key is not proof of failed suppression if a valid fallback is evidenced.

Show population, event, time window, sample size, exact identifiers as aliases, and platform-reported metric definitions. A 2/2 sample, "no warnings," or a 100% overlap label cannot establish account-wide duplicate suppression. If the required population or denominator is unavailable, report NOT VERIFIABLE. Zero qualifying actions means an undefined ratio/NOT APPLICABLE, not 100%.

A retry should retain identity for the same action; different actions need distinct identities. Compare event names, source IDs, timing, placeholders, case, whitespace, and actual outcome. Distinguish duplicated dispatch from duplicated counted conversions. Do not sum Browser and Server counts or take their maximum as a shortcut to deduplicated totals.

## Yesterday's order and revenue reconciliation

Define yesterday as the previous complete calendar date in the authoritative store time zone. State YYYY-MM-DD and [00:00, next 00:00), UTC conversion/DST where relevant, account time zone, extraction time, and event-time versus ingestion-time basis. Do not silently use last 24 hours.

Agree the purchase recognition point and eligible statuses first. Separate accepted COD from paid/confirmed/fulfilled sales. A later cancellation/refund may not reverse a previously emitted purchase event. Record failed, unpaid, pending, test, cancelled, and refunded order treatment. Preserve raw totals and justify any adjustments with evidence.

Compare store eligible orders/revenue with comparable unique purchase counts and values from the same event source, period, currency, and business definition. Campaign-attributed purchases include attribution rules and are not this denominator. If the UI/API exposes only received raw events, aggregate aliases, samples, or attributed values, do not invent a comparable unique count or revenue.

~~~text
Count ratio % = comparable platform unique purchases / eligible store orders * 100
Revenue ratio % = comparable platform purchase value / eligible store revenue * 100
Count difference = platform count - store count
Revenue difference = platform value - store value
Server order coverage % =
  distinct eligible store orders matched to a valid server purchase
  / eligible store orders * 100
~~~

Coverage requires order-identity linkage, not merely unique event IDs. Equal aggregate counts can hide a missing order and a duplicate order. When order exports exist, classify missing, duplicate, extra, late, excluded, and mismatched-value orders under stable aliases.

For zero denominators show absolute values/differences and undefined ratio/NOT APPLICABLE. Investigate nonzero events when store orders are zero. Preserve ratios above 100%. Reconcile currencies separately; do not sum SAR and USD. Convert only under an agreed exchange-rate/date policy. Use decimal/minor-unit arithmetic and currency-specific precision.

State discount, included tax, shipping and fees policy; avoid double-counting. Apply only an agreed tolerance; never invent a 95% pass threshold. Record actual platform processing guidance and a retest time for provisional days. Delay is a hypothesis until supported, not a permanent explanation.

When comparable unique counts, value, order IDs, date filters, or complete ledger data are absent, mark the affected comparison NOT VERIFIABLE. A transport or schema-validation success does not repair a missing business comparison.
