# Execution Results — SentinelTrace Expansion Pack

**Execution date:** 17 November 2026  
**Python environment:** Python 3.13.5  
**Evidence scope:** local Python code and synthetic fixtures only.

## Verified execution

- Triage-copilot unit tests: **7 passed, 0 failed**.
- Synthetic fixture: **30 alerts processed**.
- Structured suggestions: **30 valid JSON-schema outputs**.
- Deterministic mock routing: **10 TRUE_POSITIVE, 10 FALSE_POSITIVE, 10 ESCALATE**.
- Fixture label matches: **30/30 (100%)** for this deliberately constructed deterministic fixture.
- Mock triage run: completed successfully; generated JSON suggestions, Markdown notes, and a summary.
- No human analyst decisions were recorded by the non-interactive run.
- No containment actions were performed.

## Important interpretation

The 100% fixture match is a software test of a deterministic mock provider against synthetic examples designed for those rules. It is **not** an AI/LLM accuracy score, production precision/recall, real-world false-positive rate, or evidence that an Ollama model was run. The Ollama path is implemented but must be verified with a local model before making claims about it.

## SIEM status

The SPL, KQL, Sigma files, and HTML SIEM preview are documentation and illustrative outputs. No live Splunk or Microsoft Sentinel workspace was connected or queried during this execution. Validate the queries against the target workspace and record real screenshots only after doing so.

## Command results

### Unit tests

```text
test_approved_change_is_false_positive_suggestion (test_triage_copilot.TriageCopilotTests.test_approved_change_is_false_positive_suggestion) ... ok
test_extracts_iocs_without_network_lookup (test_triage_copilot.TriageCopilotTests.test_extracts_iocs_without_network_lookup) ... ok
test_ignores_ground_truth_when_suggesting (test_triage_copilot.TriageCopilotTests.test_ignores_ground_truth_when_suggesting) ... ok
test_loads_30_alert_fixture (test_triage_copilot.TriageCopilotTests.test_loads_30_alert_fixture) ... ok
test_missing_context_escalates (test_triage_copilot.TriageCopilotTests.test_missing_context_escalates) ... ok
test_mock_returns_valid_schema (test_triage_copilot.TriageCopilotTests.test_mock_returns_valid_schema) ... ok
test_rejects_invalid_verdict (test_triage_copilot.TriageCopilotTests.test_rejects_invalid_verdict) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK
```

### Evaluation

```json
{
  "evaluation_type": "deterministic mock-backend fixture check",
  "alerts": 30,
  "valid_schema_outputs": 30,
  "fixture_matches": 30,
  "fixture_match_rate": 1.0,
  "suggestion_counts": {
    "TRUE_POSITIVE": 10,
    "FALSE_POSITIVE": 10,
    "ESCALATE": 10
  },
  "important_limit": "This is not an LLM accuracy score. The mock backend uses deterministic rules and the fixture is synthetic."
}
```

### Mock triage

```text
Processed 30 alerts using mock backend.
Suggestions: /mnt/data/SentinelTrace_Expansion/outputs/copilot_demo
Human review is required. No containment actions were performed.
```
