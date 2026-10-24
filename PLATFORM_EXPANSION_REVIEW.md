# TikTok and Snapchat Expansion Review

Date: 2026-10-24. Scope: add two separate English workflows to the existing Meta package. This is a package/documentation review, not a client tracking audit.

## Delivered structure

There are now three independently usable skills, three standalone prompts, and three skill ZIPs. Each skill contains its own access/evidence, journey/capture, event-contract/calculation, and report-template references. The standard-library builder supports all platforms or --platform selection. The existing Meta prompt and ZIP remain byte-for-byte unchanged by this expansion.

All platforms retain MCP first, browser fallback for missing account metrics, exact source-ID matching, real request evidence, quantity >1 and multi-product checkout, order authorization, yesterday's sales comparison, and two deliverables.

## Platform-specific decisions

| Area | TikTok | Snapchat |
|---|---|---|
| Browser SDK | ttq and its page/track behavior | snaptr with Snap event codes |
| Purchase naming | Current Purchase; verify support/mapping of legacy CompletePayment/PlaceAnOrder | PURCHASE |
| Server schema | Events API version, event_source_id, event, properties | CAPI version; browser/v2 fields differ from v3 |
| Money/products | Unit price versus value; content_id/price within supported contents | Browser price/item_ids versus v3 value/content_ids/contents |
| Types | Current route contract and original-type evidence | Explicit num_items string and timestamp-unit checks; schema/example conflict handling |
| Deduplication | Same event/event_id, source and timing | client_dedup_id/event_id plus documented purchase transaction/order fallback |
| Quality | Native EMQ scope/scale | Native EQS scope/scale |
| Access | Probe connector for actual event metrics | Official Snap Ads MCP read-only scope does not imply all Events Manager metrics |

The strict >8.5/10 client target is retained only when a platform's native score supports that scale. No automatic conversion to percentages or categorical scores is prescribed. The 100% deduplication target always has an explicit population and evidence boundary.

## Official-source review and limitations

TikTok's [standard-event guide](https://ads.tiktok.com/resources/help/article/standard-events-parameters?lang=en), [parameter guide](https://ads.tiktok.com/resources/help/article/about-parameters?lang=en), [deduplication guidance](https://ads.tiktok.com/resources/help/article/event-deduplication?lang=en), and [monitoring guide](https://ads.tiktok.com/resources/help/article/tiktok-events-manager-monitor-and-diagnose?lang=en) were readable. Developer portal pages often returned a JavaScript shell. Indexed official examples helped identify fields, but did not establish a complete current API schema. The audit instructions require rechecking exact developer contracts and disclosing inaccessible requirements.

Snap's [CAPI parameters](https://developers.snap.com/marketing-api/Conversions-API/Parameters), [API usage](https://developers.snap.com/marketing-api/Conversions-API/UsingTheAPI), [migration guide](https://developers.snap.com/marketing-api/Conversions-API/MigrationGuide), [deduplication guide](https://developers.snap.com/marketing-api/Conversions-API/Deduplication), [validation guide](https://developers.snap.com/marketing-api/Conversions-API/VerifySetUp), and [official GTM template](https://github.com/Snapchat/snapchat-google-tag-manager/blob/main/template.tpl) were inspected. Some Business Help pages returned CSS errors. Type/example inconsistencies are explicitly called out; the instructions do not claim a complete verified browser type schema.

The [official Snap Ads MCP documentation](https://developers.snap.com/marketing-api/Ads-MCP/Introduction) describes read-only access. The skill therefore checks actual available operations and uses authorized browser access for missing diagnostic measurements.

## Validation boundary

Package validation covers skill manifests, links/resources, independent ZIP contents, deterministic generated artifacts, platform selection, and preservation of the existing Meta deliverables. Platform-specific evaluation scenarios are supplied for future model runs.

No live client browser audit, authenticated TikTok/Snap account inspection, test purchase, or end-to-end ChatGPT/Claude behavior evaluation was performed. The scenario logs deliberately remain NOT RUN. Source freshness, account permissions, tools, and actual website behavior must be checked in each audit.
