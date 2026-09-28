# Meesho Reseller Growth & Alert Intelligence Pipeline

A deterministic, offline, end-to-end monitoring pipeline implementing the four project parts.

## Requirements
- Python 3.9+
- SQLite (Python's built-in `sqlite3` or the `sqlite3` CLI)
- No API key, paid service, or hosted account is required.

## Run in order

### 1. Generate the seeded dataset
```bash
python data/generate_dataset.py
```
This creates 24 resellers, 900 orders, and `data/meesho_reseller.db`.

### 2. Run Part 1 SQL
With the SQLite CLI:
```bash
sqlite3 data/meesho_reseller.db < part1_sql/queries.sql
```
This creates the CSV outputs under `part1_sql/output/`.

If the `sqlite3` CLI is unavailable, the same SQL can be executed through Python's built-in `sqlite3` module.

### 3. Run Part 2 tests
From the repository root:
```bash
python -m pytest part2_engine/test_growth_engine.py
```
or use a standard Python test runner after adding the repository root to `PYTHONPATH`.

### 4. Run Part 4 scenarios
The repository includes split month fixtures generated from the Part 1 output:
```bash
python part4_agent/mock_agent_runner.py May part2_engine/fixtures/april_category_revenue.csv part2_engine/fixtures/may_category_revenue.csv
python part4_agent/mock_agent_runner.py June part2_engine/fixtures/may_category_revenue.csv part2_engine/fixtures/june_category_revenue.csv
```
For the hard-stop case:
```bash
python part4_agent/mock_agent_runner.py July part2_engine/fixtures/june_category_revenue.csv part2_engine/fixtures/corrupted_feed.csv
```
Run the Part 4 tests with:
```bash
python -m pytest part4_agent/test_mock_agent_runner.py
```

## Parts connection
- **Part 1 → Part 2:** SQL computes the real numbers first; the Python engine validates the feed and applies an explicit MoM rule.
- **Part 2 → Part 3:** verified growth/flag outputs become the controlled inputs for deterministic stakeholder narratives.
- **Part 3 → Part 4:** the prompt-pack structure and masking rules are used by the mock agent runner.
- **Part 4:** mirrors an Intake → Summary → Report Draft → Validate/Approval workflow with hard-stop and notification-cap guardrails.

## Offline AI narrative
The narrative layer is deterministic template filling. No LLM API is required, and the complete pipeline works with zero API keys set.

## Official project requirements
The repository intentionally uses the seeded generator and acceptance values supplied in the project brief. No seed, weights, or row counts are changed.

## Python documentation referenced
Implementation uses the Python standard-library modules `random`, `sqlite3`, `csv`, `os`, `json`, and `sys`. Official Python documentation was referenced for standard-library APIs.

## Repository contents
- `data/generate_dataset.py`, generated CSVs, SQLite database
- `part1_sql/queries.sql` and SQL outputs
- `part2_engine/growth_engine.py`, tests, fixtures
- `part3_narrative/prompt_pack.md`, narrative report, masking module
- `part4_agent/agent_spec.md`, mock agent runner
