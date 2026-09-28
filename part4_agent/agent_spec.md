# Agent Specification

## Goal
Keep Meesho category managers informed of any category whose month-on-month revenue moves beyond the 8% threshold, with a human approving every drafted message before it is considered sent.

## Tools
- `validate_feed`, `mom_growth`, `is_flagged` from Part 2.
- Part 3's deterministic prompt-pack template-fill function in the mock runner.

## Memory / State
The agent needs the previous month's revenue per category and the current run month. The previous-month feed is supplied explicitly to the runner, so state is reproducible between runs.

## Planner
1. Load the monthly revenue feed and run `validate_feed`.
2. If invalid, Hard Stop and report validation errors.
3. If valid, compute `mom_growth` for every category against the previous month.
4. Run `is_flagged` on every category.
5. Sort flagged categories by `abs(mom_pct)` descending.
6. Draft messages for at most the top 3 flagged categories.
7. Log remaining flagged categories as `suppressed, review manually`.
8. Separately log exact-boundary categories in `escalated_categories`; do not draft them.
9. Emit one structured JSON object per run.

## Feedback Loop
Drafts are held for human approval. The runner never sends a real message.

## Guardrails
- **Input:** `validate_feed` must pass before any MoM calculation.
- **Action:** no message is auto-sent; only drafts are produced and held.
- **Output:** every numeric value in a draft must trace to a Part 1/Part 2 value.

## Stopping conditions
- **Success:** drafts are produced, or zero drafts are correctly produced when nothing crosses the threshold, with traceable numbers.
- **Error:** validation returns `False`; the run is a **Hard Stop** and returns the exact validation errors.

## Agent-level Given-When-Then specifications

1. **GIVEN** April→May Ethnic Wear revenue moves from 104520.77 to 185107.61, **WHEN** the agent computes growth and flag status, **THEN** growth is 77.1 and the status is `flagged`.
2. **GIVEN** May→June Beauty & Personal Care revenue moves from 35542.11 to 37559.07, **WHEN** the agent evaluates it, **THEN** growth is 5.67 and the status is `not_flagged`.
3. **GIVEN** previous=100000 and current=108000, **WHEN** the agent evaluates the exact threshold case, **THEN** growth is exactly 8.0 and status is `escalate_exact_boundary`.
4. **GIVEN** the corrupted feed fixture, **WHEN** the agent validates it, **THEN** validation fails with exactly the three specified errors and the run Hard Stops before MoM computation.
