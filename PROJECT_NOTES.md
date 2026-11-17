# Project notes: Data Pipeline Observability Rules

**Business problem:** Dashboard consumers need to know whether reports are fresh and complete before trusting results.

**Design:** Read delivery manifests and evaluate domain-specific freshness and completeness rules.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.
