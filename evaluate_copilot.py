#!/usr/bin/env python3
"""Evaluate deterministic mock triage routing on a synthetic labelled fixture."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from triage_copilot import load_alerts, triage_one


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, default=Path("outputs/copilot_eval"))
    args = parser.parse_args()
    alerts = load_alerts(args.input)
    correct = 0
    counts = {}
    records = []
    for item in alerts:
        truth = item.get("ground_truth")
        alert = {key: value for key, value in item.items() if key != "ground_truth"}
        result = triage_one(alert, "mock", "unused", "http://127.0.0.1")
        predicted = result["suggested_verdict"]
        counts[predicted] = counts.get(predicted, 0) + 1
        matched = predicted == truth
        correct += int(matched)
        records.append({
            "alert_id": item.get("alert_id"),
            "ground_truth": truth,
            "mock_suggestion": predicted,
            "fixture_match": matched,
            "schema_valid": True
        })
    total = len(alerts)
    summary = {
        "evaluation_type": "deterministic mock-backend fixture check",
        "alerts": total,
        "valid_schema_outputs": len(records),
        "fixture_matches": correct,
        "fixture_match_rate": round(correct / total, 4) if total else None,
        "suggestion_counts": counts,
        "important_limit": "This is not an LLM accuracy score. The mock backend uses deterministic rules and the fixture is synthetic."
    }
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "evaluation.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (args.out / "per_alert_results.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
