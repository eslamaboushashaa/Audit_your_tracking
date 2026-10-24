# TikTok Event Contract and Calculations

## Contents
- Sources and version selection
- Events and browser parameters
- Events API shape and matching
- Deduplication identity
- Quality and reconciliation

## Sources and version selection

Reference review: 2026-10-24. Reopen current official documents at audit time; record accessed URL, displayed update date, SDK/API version, requirement level, field type, and evidence. Do not declare a source current merely because it is linked here.

- [Standard events](https://ads.tiktok.com/resources/help/article/standard-events-parameters?lang=en)
- [Parameters](https://ads.tiktok.com/resources/help/article/about-parameters?lang=en)
- [Pixel implementation](https://business-api.tiktok.com/portal/docs?id=1701890973258754)
- [Web parameter implementation](https://business-api.tiktok.com/portal/docs?id=1739585702922241)
- [Events API 2.0](https://business-api.tiktok.com/portal/docs?id=1771100779668482)
- [Events API advanced matching](https://business-api.tiktok.com/portal/docs?id=1799004097478658)
- [Deduplication](https://ads.tiktok.com/resources/help/article/event-deduplication?lang=en)
- [Developer deduplication](https://business-api.tiktok.com/portal/docs?id=1739584864945154)
- [Events Manager monitoring](https://ads.tiktok.com/resources/help/article/tiktok-events-manager-monitor-and-diagnose?lang=en)

Public Help Center pages were readable during preparation. Some developer pages rendered only a JavaScript shell; indexed official examples corroborated field names but did not provide a complete schema. Recheck these through an available browser; do not turn this checklist into a false claim that every type/requirement is verified. Mark unresolved contract judgments NOT VERIFIABLE and separate observed facts from provisional recommendations.

Identify Pixel SDK, native/partner integration, Events API 2.0 versus older routes, and any gateway transformations. Do not prescribe migration solely because an older name appears; confirm support and actual account mapping.

## Events and browser parameters

The current standard-events page lists ViewContent, Search, AddToCart, AddToWishlist, InitiateCheckout, AddPaymentInfo, Purchase, and CompleteRegistration for their relevant actions. Validate only features the site supports. Page-view collection uses the installed SDK's page mechanism (commonly ttq.page()); do not assume Meta's PageView spelling is a valid API event everywhere.

Current documentation uses Purchase; older implementations and some account surfaces may use CompletePayment or PlaceAnOrder. Record the actual code, intended business milestone, version, and account mapping. Do not blindly fail a supported legacy event, emit old and new names for the same conversion, or add their counts without identity evidence. A COD order-acceptance milestone can differ from payment completion.

Build an event-specific required/conditional/recommended matrix. Catalog/value optimization purposes can change requirements; missing an optional commerce field on a plain page view is not automatically a failure.

Working browser parameter checks from the parameter guide:

| Field | Type/meaning to verify |
|---|---|
| contents | Array of product objects |
| content_ids | Product ID or multiple-ID representation supported by this route |
| content_type | String product/product_group consistent with catalog identity |
| value | Number; event amount |
| price | Number; unit amount |
| currency | Supported currency string |
| content_name, content_category, search_string, description | Strings |
| quantity | Numeric units; confirm integer/route requirements |

For each contents element inspect content_id, content_name, content_category, quantity and price as supported by the SDK. Do not automatically substitute Meta's id/item_price. Verify SDK support for top-level content_ids versus per-item content_id; do not copy a documentation typo into the implementation. Treat ID values as opaque identifiers and preserve leading zeros/large-ID precision.

Use the current field schema for exact allowed types. Decode serialized arrays before classifying them. URL/form text is not proof of an original string; obtain actual ttq arguments or demonstrably linked runtime evidence. Similar application JSON does not prove the SDK received the same types if a transformation intervenes. Record unknown original types as NOT VERIFIABLE.

A at 7 x 2 and B at 11 x 1 has subtotal 25; final value is 30 only if shipping 5 belongs in the agreed value. Per-item price for A remains 7. A numeric value 7 for two newly added units is a semantic error under an added-value policy, not a type error. Do not require num_items solely because Meta uses it; independently verify total units even if TikTok's route expresses them differently.

Check exact product/variant/catalog mapping with authorized catalog evidence; cross-event ID consistency alone is insufficient.

## Events API shape and matching

The Events API 2.0 web route is commonly POST https://business-api.tiktok.com/open_api/v1.3/event/track/. Verify observed version/endpoint before judging fields. A first-party relay is not this downstream response.

Working shape to validate against the current developer schema:

| Path | Expected shape/check |
|---|---|
| event_source | String web for the web route |
| event_source_id | String identifying the intended Pixel source |
| data | Array of event objects |
| data[].event | Supported event-name string |
| data[].event_time | Integer Unix seconds; true business-action time |
| data[].event_id | Shared unique event identifier under current contract |
| data[].user | Matching-data object |
| data[].page | Page context object; URL/referrer when supported |
| data[].properties | Ecommerce object, with route-specific types |

Use the current schema for required fields, timestamp age/future limits, numeric types, enums, nesting, and response semantics. Do not use CAPI custom_data/user_data or event_name merely because another platform does. Older API envelopes can differ; inspect actual request construction and current support.

Within properties review value, currency, content_type, contents, nested content_id/price/quantity, and any supported order reference. Compare the transformed server payload with browser payload and actual order. Redact Access-Token and all credentials.

For user matching review supported email, phone, external_id, IP, user agent, click ID, and cookie identifiers. Inspect ttclid and _ttp handling and the current server fields (commonly user.ttclid and user.ttp). Confirm exact shape and hash requirement per field/route. Do not derive server hash rules from browser automatic matching behavior. Check normalization before hashing, SDK auto-hashing versus prehashed input, and double hashing. IP/UA and click/cookie identifiers must not be indiscriminately hashed like contact details.

Record valid presence/format, per-signal coverage denominator, consent state, matching source, and observed EMQ separately. A direct visit lacking a click ID is not automatically defective. Validate authorized test data locally and report only redacted validity/equality outcomes.

Inspect HTTP and application-level API result, per-event errors/warnings when available, batch scope, request/trace ID, and matching account receipt. HTTP 200 with an error body is not a pass. A successful test event is not proof that production orders are received or counted.

## Deduplication identity

TikTok's documented shared-key mechanism uses the same event and event_id across copies. Scope to the same source, business action, and permitted timing. In the browser verify the installed SDK's event-ID options placement; an event_id sitting in ecommerce properties alone does not prove it became the dedup key. Compare it with data[].event_id in Events API.

The Help Center describes 48-hour duplicate handling and a qualified cross-source merge/dedup timing statement. Recheck current developer conditions and observed processing; do not introduce artificial delivery delays based on a simplified reading.

Keep the same ID across retries of one event, distinct IDs for separate actions, and matching event names across paired routes. Purchase and CompletePayment are not proven identical dedup keys simply because both describe conversion. Confirm any platform normalization before concluding equivalence.

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
