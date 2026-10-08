# User brief and research — 8 October 2026

State: RESEARCHED → BUILDING.

User: Frontend and platform engineers reviewing CSP deployment changes.

Painful task: Changing default-src or child-src affects inherited directives; text diffs can hide which effective lists changed.

Smallest useful capability: Compare ordered independently enforced policy lists with effective directive fallback origins, first-duplicate handling and added/removed source tokens.

Demand is inferred from the documented workflows and review risks. No verified request for this product, adoption, performance advantage or exhaustive feature gap is claimed. Search and repository/README/code/issue reads occurred on 8 October 2026; current exact stars and last-push timestamps below are observations, not quality scores.

Queries: `content security policy evaluator sort:stars; csp-evaluator in:name sort:stars`. Live GitHub search used `sort:stars`. Broad queries return unrelated repository/readme matches; irrelevant results were excluded. Coverage is limited, not an exhaustive global ranking. The highest-star relevant comparable among those examined is [google/csp-evaluator](https://github.com/google/csp-evaluator) at 405 stars.

| Comparable | Stars | Last push (UTC) | License | Workflow, setup, capabilities and tradeoffs |
|---|---:|---|---|---|
| [google/csp-evaluator](https://github.com/google/csp-evaluator) | 405 | 2026-05-26T12:52:22Z | Apache-2.0 | TypeScript parser and security evaluator with npm install and API example. Detects known security weaknesses; our representation diff does not make a security verdict. |
| [shapesecurity/salvation](https://github.com/shapesecurity/salvation) | 74 | 2025-11-25T20:36:04Z | Apache-2.0 | Java CSP parser/manipulation/URL-permission APIs with Maven setup and examples. Related HtmlUnit fork says upstream no longer actively maintained; most recent push alone does not prove support. |
| [HtmlUnit/htmlunit-csp](https://github.com/HtmlUnit/htmlunit-csp) | 5 | 2026-08-29T14:35:32Z | Apache-2.0 | Java CSP3 parser and enforcement-oriented APIs, including independently enforced policy lists and origin-bound checks. Recently updated fork; richer execution semantics than our token-list diff. |

Reliability/support observations are limited to public docs, latest source and open issue samples; alternatives were not installed or benchmarked in this run. Examples prove our behavior only. No comparative speed, memory, accuracy or time-to-result measurement was made. Licenses are metadata observations; no competitor implementation/prose was reused.

Acceptance: documented clean install; accepted example; meaningful rejected/input-error examples; deterministic JSON reports; core invariants covered by the unit tests; all remote matrix checks must pass on the intended default head before LIVE. The exact scope/non-goals are in README.md.

Discovery path: relevant GitHub topics and a clear README/linked portfolio index. No messages or third-party issue advertising planned, and no organic growth promise.

Portfolio distinction: compared against all 143 existing repository names/descriptions and relevant CSV/HTTP/parser tools. This is not a fork or a variant of an existing launch. The five candidates address spatial delivery, cache deployment intent, CSP inheritance changes, crawler route expectations and cross-export identifier mapping respectively. masklink-audit does not reconcile numeric CSV differences like table-reconcile, transform data or copy a redaction engine. They are separate user tasks, not subdivisions of one product.

## Commit-linked observations

- [google/csp-evaluator source snapshot](https://github.com/google/csp-evaluator/tree/ad530f3ae5473f9e03c8bf500ee0ada8d9e9b822) — open issue sample: [#79](https://github.com/google/csp-evaluator/issues/79), [#71](https://github.com/google/csp-evaluator/issues/71), [#64](https://github.com/google/csp-evaluator/issues/64).
- [shapesecurity/salvation source snapshot](https://github.com/shapesecurity/salvation/tree/0b71b9197d399c031652265b4deb7b7a99b4c0e2) — open issue sample: [#260](https://github.com/shapesecurity/salvation/issues/260), [#259](https://github.com/shapesecurity/salvation/issues/259), [#258](https://github.com/shapesecurity/salvation/issues/258).
- [HtmlUnit/htmlunit-csp source snapshot](https://github.com/HtmlUnit/htmlunit-csp/tree/25984132da03b15e227154564de86785de62f058) — open issue sample: [#12](https://github.com/HtmlUnit/htmlunit-csp/issues/12).

Standards consulted: [GeoJSON RFC 7946](https://www.rfc-editor.org/rfc/rfc7946.html), [HTTP caching RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html), [Robots RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html), [CSP3](https://www.w3.org/TR/CSP3/). Only the relevant standard informs each bounded tool; conformance is not claimed.
