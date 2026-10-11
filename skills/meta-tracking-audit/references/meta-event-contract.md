# Meta Event Contract and Calculations

## Contents
- Current-source rule
- Event triggers and applicability
- Parameter and type validation
- CAPI and matching signals
- EMQ
- Deduplication
- Yesterday's sales reconciliation

## Current-source rule

At audit time open the relevant official Meta references. Record access date, displayed update date if available, API/SDK version where known, exact field path, event, transport, requirement level, and type. Use these starting points; follow official redirects if URLs change:

- https://developers.facebook.com/documentation/meta-pixel/reference#standard-events
- https://developers.facebook.com/docs/marketing-api/conversions-api/parameters
- https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event
- https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters
- https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/custom-data
- https://developers.facebook.com/documentation/ads-commerce/conversions-api/deduplicate-pixel-and-server-events

The tables below are working checklists, not a claim that the current documentation has been verified. Resolve field-specific allowed types, required/recommended status, limits, and conditional rules from the current official contract. If inaccessible, state "current contract not independently verified" for affected judgments and separate observed implementation facts from provisional recommendations. Never fabricate a quotation, requirement, or API capability.

## Event triggers and applicability

| Action | Meta event to check | Expected business state |
|---|---|---|
| Logical page/virtual navigation | PageView | Page becomes active under agreed navigation policy |
| Product detail | ViewContent | Correct product data displayed |
| Submitted search | Search | Submitted query and established results state |
| Add product | AddToCart | Cart mutation succeeds |
| Wishlist addition | AddToWishlist | Addition succeeds, if feature exists |
| Enter checkout | InitiateCheckout | Checkout actually begins |
| Payment information/method | AddPaymentInfo | Agreed payment state accepted, including COD semantics if applicable |
| Purchase | Purchase | Successful order/payment state under approved recognition policy |
| Registration | CompleteRegistration | Registration succeeds, if in scope |

Add other current standard events for supported business features. Do not map GA4 names such as view_item, begin_checkout, or add_payment_info directly into Meta standard names. Do not describe ViewCart, RemoveFromCart, or AddShippingInfo as Meta standard events without current documentation; these may require custom events.

Not every site needs every event or every listed parameter. Build an applicability/requirement matrix by event and purpose, including catalog/dynamic-ad use. Missing optional fields are not automatically failures. Purchase value and currency deserve explicit checks against the current Purchase contract. For catalog use, verify required content identity fields and actual feed IDs.

## Parameter and type validation

For each event, record raw wire value, decoded value, known pre-serialization type, expected route-specific type, requirement level, requirement source, semantic result, and evidence ID. Use "unknown" for a type not established.

| Browser field | Working type check | Business validation |
|---|---|---|
| value | Number | Finite monetary value for this event; not formatted text |
| currency | String | Valid ISO 4217 code for the amount |
| content_ids | Array; validate allowed element types | Product/variant identity policy; do not collapse an array into comma-separated text |
| contents | Array of objects | All relevant products at this stage |
| contents[].id | Validate accepted ID type for route; preserve identity | Exact catalog/variant mapping; avoid losing leading zeros or large-ID precision |
| contents[].quantity | Numeric; positive whole units for ordinary unit products | Actual units for this action |
| contents[].item_price | Number when supplied | Unit price, not line total |
| num_items | Integer when supplied | Sum of units, not number of distinct lines |
| content_type | String | Allowed product/product_group value matching identity policy |
| content_name | String | Actual product/content |
| content_category | String under the Pixel contract | Meaningful category; do not assume arrays are accepted |
| search_string | String | Actual submitted query, checked for sensitive content |
| order_id | Validate current route contract; stable reference | Order association; not automatic deduplication identity |
| Fourth fbq argument: eventID | String for shared-ID deduplication | Stable for the same action and its retry; different for distinct actions |

Browser example shape, illustrative only:

~~~javascript
fbq('track', 'Purchase',
  { value: 30, currency: 'SAR',
    contents: [{ id: 'A', quantity: 2, item_price: 7 },
               { id: 'B', quantity: 1, item_price: 11 }],
    content_ids: ['A', 'B'], content_type: 'product', num_items: 3 },
  { eventID: 'purchase-test-001' });
~~~

This illustrates placement/types, not a command to execute. Confirm optional/support requirements before prescribing fields. The example includes shipping 5 in value by an illustrative policy.

Query/form encoding represents fields as text. URL-decode and parse nested JSON such as content_ids/contents before classification. Corroborate original types using the real SDK call or demonstrably linked runtime state. Source code alone is SOURCE-ONLY; similar first-party JSON does not prove what fbq received if a transformation intervenes.

If native types cannot be observed, report decoded wire correctness separately and mark the original-type check NOT VERIFIABLE. Reject malformed JSON, nested objects serialized twice, null/empty required fields, NaN/Infinity, wrong currency scales, and inconsistent minor/major units when evidence supports the defect.

A numeric value of 7 for two units at 7 can be Type PASS / Semantic FAIL. Currency rounding is a semantic/precision check: use the actual currency precision, and do not prescribe toFixed() alone since it returns a string.

## CAPI and matching signals

Validate the server route independently; do not copy the browser schema indiscriminately.

| Path | Working shape/type check | Verification |
|---|---|---|
| data | Array of event objects | Correct batch boundaries and event counts |
| data[].event_name | String | Correct name/case; same event as browser when paired |
| data[].event_time | Integer Unix seconds | Real action time, not milliseconds or retry time; current allowed age/future rules |
| data[].event_id | String for shared-ID deduplication | Exact match with browser eventID for same action |
| data[].action_source | Allowed string | Actual source, typically website here |
| data[].event_source_url | URL string when required by source | Correct source; no sensitive query values |
| data[].user_data | Object | Required/conditional customer fields, correct placement |
| data[].custom_data | Object | Commerce data under CAPI's current field-specific schema |

Within custom_data validate value, currency, content_ids, contents and nested id/quantity/item_price, num_items, content_type, and order_id against CAPI's own accepted types. Explicitly record any SDK coercion, array-versus-scalar differences, and numeric-string allowances the current API supports. A tolerated transport representation and a preferred SDK input are not the same contract.

For website user_data assess supported matching fields such as em, ph, fn, ln, ct, st, zp, country, external_id, fbp, fbc, client_ip_address, and client_user_agent. For each, record:

| Signal | Required/conditional/recommended | Actual scalar/array shape | Normalization | Hash rule and evidence | Valid presence | Coverage and denominator |
|---|---|---|---|---|---|---|

Check current per-field normalization and scalar/array rules. Normalize before SHA-256 for fields requiring it; do not assume every field has identical rules. Distinguish SDK automatic hashing from prehashed input to catch double hashing. Never hash fbp, fbc, IP, or user agent when their contract requires unhashed values. Check client origin rather than proxy/server identity for network signals using trusted evidence.

Do not fabricate fbc on a direct visit or collect additional sensitive information solely to improve EMQ. Verify cookies/click IDs and timestamp formats when applicable, lawful/authorized collection, and signal continuity across domains. Do not expose raw identifiers or matching hashes in reports.

Separate signal presence, valid type/normalization/hash, eligible-event coverage, and the observed EMQ outcome. A signal count is not proof of effective match quality.

Require real Meta response or matching account evidence for receipt claims. Distinguish first-party enqueue, downstream submission, Meta receipt, processing, deduplication, and reporting. Server logs must show the relevant downstream action/response, not only an outgoing job. Inspect errors, warnings, retry handling, integration ownership, and payload losses at each transformation.

## EMQ

Client target: **strictly above 8.5/10 (> 8.5)** for applicable business-critical Server events, especially Purchase. A score of exactly 8.5 does not meet this target. This is the client's internal target, not a universal Meta acceptance rule.

Capture score, exact event, source, Dataset, period, extraction time, displayed precision, recommendations, and evidence. A rounded score cannot justify a more precise claim. If score is absent, mark NOT VERIFIABLE; if CAPI is confirmed absent, use NOT APPLICABLE for the score. Never infer EMQ from browser fields or average all events to hide weak Purchase quality.

## Deduplication

Client target: 100% for the defined population intentionally sent through Browser and Server. Evaluate separately:

1. Delivery of both expected sources.
2. Shared-ID key coverage/validity.
3. Platform duplicate suppression outcome.
4. Account-wide metric and its actual denominator.

For paired events verify same Dataset, same event_name, browser eventID equal to CAPI event_id, stable identity for the same action/retry, unique identity across distinct actions, consistent event timing, and compatible business content. Validate current Meta timing/retention rules; do not invent a time window.

Do not use order_id alone as proof of deduplication. If an integration claims a different documented deduplication mechanism, verify its current support, exact conditions, and Meta outcome; distinguish a departure from the shared-ID design from proven duplicate counting.

~~~text
Sample key coverage % =
  observed intended dual-source actions with both valid matching IDs
  / all intended dual-source actions in the tested sample * 100
~~~

Include missing-source actions in the denominator. Do not restrict it to already-matched pairs. If no actions qualify, use NOT APPLICABLE with denominator 0, not 100%. If the intended population cannot be enumerated, coverage is NOT VERIFIABLE.

Report "2/2 sampled actions, 100% sample key coverage" only for that sample. It does not establish account-wide 100% deduplication.

Record Events Manager's exact labels and definitions for overlap, key coverage, diagnostics, and deduplication. They are different metrics. If the interface exposes no true suppression measure or denominator, mark the client's account-wide target NOT VERIFIABLE. "No warnings" or "100% overlap" alone cannot meet it. Do not demand that 100% of all raw browser+server submissions disappear; one retained event per genuine action is intended.

## Yesterday's sales reconciliation

Use the previous complete calendar day in the agreed store time zone, stated as YYYY-MM-DD and an explicit local interval [00:00, next 00:00). Align account time zone, UTC conversion, DST where relevant, event_time vs ingestion time, and extraction timestamp. Never silently use last 24 hours.

Define the eligible order population and Purchase recognition policy before comparing. Record cancellations, refunds, pending COD, unpaid, failed, test orders, revenue components, and currency. A later cancellation/refund may not retroactively remove a previously sent Purchase; do not treat current net sales as automatically comparable to accepted-order events. Preserve both raw totals and any evidence-based adjustments.

Collect:
- Store eligible orders/revenue with a PII-free order ledger when possible.
- Meta Browser and Server received counts, explicitly deduplicated Purchase count if available, comparable value/currency if available, source labels, filters, and delays.

Never estimate deduplicated count by adding Browser+Server or taking their maximum. Do not substitute Ads Manager attributed purchases. If Events Manager does not expose comparable unique counts or revenue, mark the corresponding comparison NOT VERIFIABLE; do not manufacture it from sample values or averages.

~~~text
Count ratio % = comparable Meta unique Purchase count / eligible store order count * 100
Revenue ratio % = comparable Meta Purchase value / eligible store revenue * 100
Count difference = Meta count - store count
Revenue difference = Meta value - store revenue
Matched server order coverage % =
  distinct eligible store orders with at least one valid matched Server Purchase
  / eligible store orders * 100
~~~

Aggregate ratios are reconciliation ratios, not proof of order coverage. Equal totals can hide one missing and one duplicate order. True coverage requires matching eligible order identities; unique server event IDs alone cannot establish order coverage.

For denominator 0, report ratio NOT APPLICABLE (undefined), show absolute amounts and differences, and investigate any nonzero Meta events/value. Do not divide by zero or report an invented 100%. For nonzero denominators, show values above 100% rather than clipping.

Reconcile each currency separately. Do not sum different currencies or convert without an agreed exchange-rate source, date, and policy. Use integer minor units or decimal arithmetic with documented currency precision and a client-approved tolerance; do not invent a 95% acceptance threshold.

If delays make the day provisional, record the actual platform guidance and a retest time. Do not permanently attribute unexplained gaps to delay. Categorize missing, duplicate, extra, mismatched-value, delayed, and excluded orders when identity-level evidence exists. For aggregate-only evidence, state that identity-level reconciliation remains unverified.
