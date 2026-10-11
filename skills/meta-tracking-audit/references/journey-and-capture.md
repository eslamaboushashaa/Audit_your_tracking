# Journey and Network Capture

## Contents
- Prepare the capture
- Test matrix
- Arithmetic and duplicate checks
- Consent, browser, and boundary tests

## Prepare the capture

Identify actual tools for navigation, interaction, Network requests/responses, runtime evaluation, and authenticated account access. Prefer Chrome and its available Network/DevTools integration. Do not equate a browser extension or screenshot tool with Network access.

Inventory the platform, fbevents.js/fbq initialization, native integration, GTM, partner gateway, first-party endpoints, server-side GTM, and other observed sources. Multiple install paths are a duplicate risk, not proof of duplicates.

Before each action:
1. Open Network capture; preserve across navigation if supported.
2. Record precise start time, browser/version, device/viewport, URLs, consent, login, extensions/blockers, and test data state.
3. Capture baseline events, then perform one real action.
4. Wait for its application outcome and asynchronous requests; record the observation window.
5. Preserve request URL/method, parameters/body, response/status, initiator, destination ID, and related state.
6. Correlate SDK arguments, data layer, cart/order response, browser collector, first-party gateway, server logs, and Meta evidence where available.

Separate event payloads from SDK loading, metadata, redirects, OPTIONS/preflight, diagnostics, and retries. One request may contain multiple events; multiple requests may describe one logical event. Count semantic actions and payloads, not HTTP lines.

Use platform-supported passive inspection. If observing fbq arguments requires a local wrapper, preserve original behavior, record the instrumentation, and corroborate with unmodified requests. Never manually invoke fbq or replay production requests to demonstrate event success. A data-layer object or source snippet supports the type conclusion only when demonstrably linked to the dispatched event.

## Test matrix

| Case | Action/outcome | Expected checks |
|---|---|---|
| J01 | Homepage then category/product navigation | Correct PageView count under agreed navigation policy; no accidental Purchase |
| J02 | Product A and selected variant displayed | ViewContent for the displayed product/variant, correct ID/value/currency |
| J03 | Search submitted; safe zero-results query if supported | Search query and timing; avoid per-keystroke inflation |
| J04 | Add product A, quantity 1 | AddToCart after success; added-unit value and item identity |
| J05 | Add an in-stock product at quantity 2 or more | Quantity and monetary arithmetic; distinguish incremental addition from cart total |
| J06 | Add a distinct product B; update quantity if supported | Both lines preserved; cart response and emitted events consistent |
| J07 | Enter checkout with at least two distinct products, one quantity >1 where possible | InitiateCheckout at checkout entry; all lines, quantities, total units and correct stage value |
| J08 | Select shipping and accepted payment state | AddPaymentInfo under agreed semantics; shipping/discount/fees reflected consistently |
| J09 | One authorized order succeeds | Purchase at agreed business recognition point with stable order ID, full contents and final value |
| J10 | Revisit/reload confirmed success page safely | No second order or independently counted Purchase; stable identity for legitimate retry |
| J11 | Wishlist, registration, or other in-scope feature | Applicable current Meta standard event after success |
| J12 | Safe failed action/form validation | No success event when the action fails |

Record expected count, actual count, status, evidence IDs, and blocker for each case. If stock makes J05/J07 impossible, document attempts and request alternatives; do not silently substitute a single-product checkout as equivalent.

For J08, agree whether a COD selection constitutes accepted payment information. Do not declare missing AddPaymentInfo a defect until the actual payment flow and intended event contract are known.

For J09, distinguish accepted COD order from paid/confirmed/fulfilled revenue. Purchase timing must match the client's approved recognition rule. Do not force a paid-order requirement onto a COD acceptance contract or treat an unaccepted submit click as a Purchase.

For J10, reload only a safe confirmation GET or equivalent view, never an order-submission POST or a browser "resubmit form" action. A retried event with stable dedup identity may be valid; a second request alone does not prove a second counted purchase.

Do not create another order just to replace an incomplete capture. Record the existing order and ask if an additional order is necessary. Provide the cancellation reference privately; report whether cancellation is pending, user-owned, or confirmed. Do not claim cancellation without evidence.

## Arithmetic and duplicate checks

Record ID/SKU/variant, quantity, unit price, line discount, subtotal, order discount, tax, shipping, and fees. Identify whether displayed prices already include tax and whether discounts have already been applied; avoid double subtraction.

A cart with A at 7 x 2 and B at 11 x 1 has three units and an item subtotal of 25. If policy includes shipping 5 and excludes nothing else, final value is 30. Item A's item_price remains 7. This is an illustrative test fixture, not observed client data.

Compare every available layer: UI, cart/checkout API, SDK call, browser request, server payload, Meta sample. Catalog matching requires actual authorized catalog evidence; matching across website events alone cannot prove catalog compatibility.

Check duplicate installation, double-click handling where safe, SPA/history navigation, server retries, confirmation reload, and repeated payment selection. Record whether identical event IDs are reused for the same action and changed for distinct actions.

## Consent, browser, and boundary tests

Test only states supported and permitted by the website/user scope. Do not bypass consent controls or browser privacy protections.

- Observe initial consent state, rejection, acceptance, and returning consent when supported. Compare actual collection against the site's stated consent design; do not make a legal compliance verdict.
- A prevented request under denied consent/ad blocking is not automatically broken tracking. Separate expected suppression, transport blocking, and missing implementation.
- Label direct visits vs genuine authorized ad-click visits. Do not fabricate fbclid/fbc to improve scores. Missing fbc on a direct visit is not automatically a defect.
- Check identifier continuity and event-source URL across checkout domains, redirects, iframes, and hosted payment/confirmation pages when applicable.
- Record desktop/mobile and browser scope. A narrow desktop result does not establish Safari/mobile coverage.
- Check that sensitive data is absent from URL query strings, event names, custom_data, content names, and other inappropriate fields.

Mark untested states explicitly; prioritize expanded testing when a finding or architecture warrants it.
