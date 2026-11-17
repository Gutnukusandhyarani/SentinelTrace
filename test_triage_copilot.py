import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from triage_copilot import (
    extract_iocs, load_alerts, mock_suggestion, triage_one, validate_suggestion
)


class TriageCopilotTests(unittest.TestCase):
    def test_mock_returns_valid_schema(self):
        result = mock_suggestion({
            "alert_id": "T-1", "summary": "SSH failure burst",
            "rule_id": "ST-DET-01", "severity": "High",
            "signals": {"success_after_failures": True, "failed_attempts": 6}
        })
        validate_suggestion(result)
        self.assertEqual(result["suggested_verdict"], "TRUE_POSITIVE")

    def test_approved_change_is_false_positive_suggestion(self):
        result = mock_suggestion({
            "alert_id": "T-2", "summary": "Approved change",
            "signals": {"approved_change": True}
        })
        self.assertEqual(result["suggested_verdict"], "FALSE_POSITIVE")

    def test_missing_context_escalates(self):
        result = mock_suggestion({"alert_id": "T-3", "summary": "Unknown activity", "signals": {}})
        self.assertEqual(result["suggested_verdict"], "ESCALATE")

    def test_extracts_iocs_without_network_lookup(self):
        iocs = extract_iocs({
            "summary": "Observed 203.0.113.9 contacting example.test",
            "hash": "a" * 64
        })
        values = {(item["type"], item["value"]) for item in iocs}
        self.assertIn(("ip", "203.0.113.9"), values)
        self.assertIn(("domain", "example.test"), values)
        self.assertIn(("hash", "a" * 64), values)

    def test_rejects_invalid_verdict(self):
        bad = mock_suggestion({"alert_id": "T-4", "signals": {}})
        bad["suggested_verdict"] = "BLOCK"
        with self.assertRaises(ValueError):
            validate_suggestion(bad)

    def test_ignores_ground_truth_when_suggesting(self):
        alert = {
            "alert_id": "T-5", "summary": "No context",
            "ground_truth": "TRUE_POSITIVE", "signals": {}
        }
        self.assertEqual(triage_one(alert, "mock", "unused", "http://127.0.0.1")["suggested_verdict"], "ESCALATE")

    def test_loads_30_alert_fixture(self):
        data = load_alerts(ROOT / "data" / "triage_eval_30.json")
        self.assertEqual(len(data), 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
