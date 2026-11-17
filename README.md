# Data Pipeline Observability Rules

Runs freshness, completeness, and row-count checks against daily pipeline delivery manifests.  
Produces a compact health report with concrete breach reasons and configurable thresholds.

## Problem

Dashboard consumers need to know whether reports are fresh and complete before trusting results.

## Solution and design

Read delivery manifests and evaluate domain-specific freshness and completeness rules.

**Stack:** Python, data observability, reliability engineering, SLAs

## Quick start

Requires Python 3.11+ (standard library only for the local demo).

```bash
python main.py
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same tests on pushes and pull requests.

## Project layout

- `main.py`: core processing and a small command-line demonstration
- `data/`, `seeds/`, `models/`, `sql/`, `infra/`, `dags/` or `powerbi/`: included only where relevant
- `tests/`: fixture-based expected-value and repeatability checks

## Engineering decisions

- Narrow scope, realistic field names, and synthetic reproducible inputs
- No credentials, customer records, patient data, API tokens, or paid cloud resources
- Visible business logic and deterministic fixtures rather than screenshots of unverifiable dashboards

## Limits and next iteration

Small synthetic fixtures are used for reproducibility. Production systems would need credential management, data volume testing, monitoring, and access controls.

A production hardening path would add larger-scale fixtures, alerting, operational runbooks, robust error handling, and integration tests against the real deployment target.

## Portfolio integrity

This is an independently reproducible **portfolio demonstration**, not a claim that these files are employer code or that a cloud workload has been deployed. The fixture data is synthetic.
