# Reusable Narrative Prompt Pack

## Trigger
Start only when a category's `is_flagged` result is `"flagged"`. Exact-boundary results (`"escalate_exact_boundary"`) are held for human review and do not trigger this narrative.

## Input list
- `{category}`
- `{previous_revenue}`
- `{current_revenue}`
- `{mom_pct}`
- `{month}`
- `{prev_month}`

## Prompt
Using only the supplied placeholders, write a stakeholder update for a regional manager in **Context → Insight → Implication** format. Context must name the category and the comparison period `{month}` vs `{prev_month}`. Insight must state `{mom_pct}` exactly and label it explicitly as a **fact**. Implication must give one concrete next action. If a possible cause is proposed, label it explicitly as a **hypothesis** because the supplied revenue data alone does not prove causation. Do not state any number that is not one of the supplied placeholder values. Do not identify any reseller by raw name; use a coded alias if a reseller must be referenced.

## Checklist
1. Every number in the draft matches a supplied placeholder value exactly.
2. The percentage is labeled as a fact, not a hypothesis.
3. Any proposed cause is labeled as a hypothesis.
4. The next action names a concrete check or action rather than saying only “look into it”.
5. The category and both months are explicit.
6. No raw reseller name appears in the external-facing draft.
