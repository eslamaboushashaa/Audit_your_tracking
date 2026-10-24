# Snapchat Journey and Network Capture

## Contents
- Prepare capture
- Test matrix
- Arithmetic and business semantics
- Boundary and privacy states

## Prepare capture

Identify the actual browser/Network/runtime tools. Prefer Chrome with request and response inspection. Extensions are supporting evidence, not substitutes for payload inspection. Inventory snaptr, native integrations, GTM, first-party routes and partner gateways; multiple installations suggest a duplicate risk, not proof.

Open Network capture before each action; preserve logs across navigation where supported. Record browser/version, viewport/device, consent, login, blockers/extensions, direct/ad-click origin, and test start time. Observe a baseline, perform one real action, wait for its outcome and asynchronous delivery, then retain evidence before navigating.

Correlate SDK arguments, data layer, cart/checkout response, browser collector, first-party gateway, downstream server request, and account sample. Any runtime wrapper must preserve SDK behavior and be disclosed; corroborate with unmodified traffic. Do not manually call snaptr, replay production requests, or use guessed checkout APIs to create evidence.

Count semantic events separately from script loading, metadata, preflight, redirects, batching, transport retries, and diagnostics. Record observation-window limits. A first-party 200 is only that endpoint's response.

## Test matrix

| Case | Real action | Expected platform event/check |
|---|---|---|
| J01 | Homepage and logical/virtual navigation | PAGE_VIEW; intended source, reasonable logical count, no accidental purchase |
| J02 | Product A and variant displayed | VIEW_CONTENT; ID, variant, price and currency reflect the actual item |
| J03 | Search submitted; safe zero-results query when available | SEARCH; query and results state; no per-keystroke inflation |
| J04 | Successful add of quantity 1 | ADD_CART; event after successful mutation |
| J05 | Successful add of quantity 2 or more | ADD_CART; distinguish incremental amount from whole-cart total |
| J06 | Add distinct product B and update quantity | Preserve both products and their identity/quantity policy |
| J07 | Enter checkout with two distinct products and one quantity >1 | START_CHECKOUT; correct stage value, all items, total units |
| J08 | Shipping then accepted payment state | ADD_BILLING; explicit COD semantics, no event merely on option display |
| J09 | One authorized successful order | PURCHASE; stable order, recognition policy, final value and all items |
| J10 | Safe confirmation-page revisit/reload | No extra order or separately counted purchase; stable retry identity |
| J11 | Wishlist/registration if applicable | ADD_TO_WISHLIST / SIGN_UP; successful feature outcome |
| J12 | Safe validation failure or failed action | No success event when underlying business action fails |

For each case record expected/actual logical count, routes, observed parameters, evidence, and result. Add other standard events only for actual relevant site features. Confirm version-specific names in the contract reference before declaring an event missing.

If stock or checkout prevents multi-product/quantity tests, record attempts and blocker; a one-product checkout is not equivalent. Do not create an additional order to compensate for missing capture without authorization.

## Arithmetic and business semantics

Record product/variant/SKU, unit price, quantity, discounts, tax treatment, shipping, fees, currency, line totals, cart subtotal, checkout-stage value, and final order value. Avoid double-subtracting discounts or adding included tax.

Illustrative fixture: A at 7 x 2 plus B at 11 x 1 means subtotal 25 and three units. Shipping 5 makes 30 only if the approved value policy includes it. For Snap Purchase the browser price is the agreed transaction amount; it is not automatically one unit's price. CAPI v3 value represents the agreed transaction value.

Compare UI, application/cart API, SDK input, decoded collector, server payload, and platform evidence. Verify every product survives transformation; do not require unsupported browser item structures solely because another platform supports them. Catalog compatibility needs actual connected-catalog evidence, not just matching IDs between two website events.

Document accepted-order versus paid/confirmed/fulfilled recognition, particularly COD. Failed submit clicks are not purchases; an accepted COD order is not proof of collected revenue. Agree what the payment-information event means before judging it.

Reload only a safe confirmation GET/equivalent view. Never resubmit an order POST or confirm a browser resubmission dialog. A second request alone is not a second counted purchase; inspect event identity and platform outcome.

Record cancellation owner and status; do not claim the order was cancelled without evidence.

## Boundary and privacy states

Assess supported permitted consent states, returning consent, SPA navigation, safe repeated actions, native/tag duplication, server retries, hosted checkout, cross-domain redirects, iframes, and confirmation-page availability. Document mobile/Safari scope rather than extrapolating from one desktop browser.

Distinguish blocked-by-consent or blocked-by-browser traffic from missing implementation. Follow the site's consent design without bypassing it; technical observations are not a legal compliance verdict.

Label direct visits and genuine authorized ad-click visits. Do not fabricate ScCid or _scid to improve matching. Missing click ID on a direct visit is not automatically defective. Check persistence across permitted checkout boundaries, using the current platform-specific server fields.

Check for PII in event names, content names, page URLs, ecommerce payloads, and other inappropriate fields. Consent denial is not permission to send server events instead; evaluate both routes under the agreed consent design. Mark untested states explicitly.
