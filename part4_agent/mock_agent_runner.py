import csv
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "part2_engine"))
from growth_engine import validate_feed, mom_growth, is_flagged

def _read_feed(path):
    with open(path, newline="", encoding="utf-8") as f:
        return {row["category"]: row for row in csv.DictReader(f)}

def _draft(category, previous_revenue, current_revenue, mom_pct, month, prev_month):
    return (
        f"Context: {category} revenue is compared for {month} vs. {prev_month}. "
        f"Insight (fact): {category} revenue moved by {mom_pct}% month-on-month. "
        f"Implication (hypothesis): compare order volume and reseller-level contribution "
        f"between {prev_month} and {month} to identify whether the movement is broad-based "
        f"or concentrated before taking action."
    )

def run(month: str, previous_month_csv: str, current_month_csv: str) -> dict:
    valid, errors = validate_feed(current_month_csv)
    if not valid:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop",
        }

    prev = _read_feed(previous_month_csv)
    curr = _read_feed(current_month_csv)
    flagged = []
    suppressed = []
    escalated = []

    for category, current_row in curr.items():
        if category not in prev:
            continue
        previous_revenue = float(prev[category]["revenue"])
        current_revenue = float(current_row["revenue"])
        pct = mom_growth(previous_revenue, current_revenue)
        status = is_flagged(pct)
        if status == "flagged":
            flagged.append((category, pct, previous_revenue, current_revenue))
        elif status == "escalate_exact_boundary":
            escalated.append(category)

    flagged.sort(key=lambda x: abs(x[1]), reverse=True)
    drafted_entries = []
    for category, pct, previous_revenue, current_revenue in flagged[:3]:
        drafted_entries.append({
            "category": category,
            "mom_pct": pct,
            "previous_revenue": previous_revenue,
            "current_revenue": current_revenue,
            "drafted": True,
            "message": _draft(category, previous_revenue, current_revenue, pct, month, _previous_month(month)),
        })

    suppressed = [category for category, *_ in flagged[3:]]
    return {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": drafted_entries,
        "suppressed_categories": suppressed,
        "escalated_categories": escalated,
        "action_taken": "drafted_and_held_for_approval",
    }

def _previous_month(month):
    return {"May": "April", "June": "May"}.get(month, "previous month")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("Usage: python mock_agent_runner.py <month> <previous_csv> <current_csv>")
    print(json.dumps(run(sys.argv[1], sys.argv[2], sys.argv[3]), indent=2))
