# Evidence Index

| Artifact | Evidence type | Provenance |
|---|---|---|
| `outputs/copilot_demo/suggestions.json` | Verified local execution | Produced by running `src/triage_copilot.py` with deterministic `mock` backend on the included synthetic fixture |
| `outputs/copilot_demo/triage_notes.md` | Verified local execution | Draft analyst notes from the same mock run; no human decisions |
| `outputs/copilot_demo/summary.json` | Verified local execution | Run summary from the same mock run |
| `outputs/copilot_eval/evaluation.json` | Verified local execution | 30-alert deterministic fixture evaluation; not an LLM score |
| `outputs/illustrative-siem/siem_alert_preview.html` | Illustrative only | Hand-authored mock view; not a Splunk/Sentinel screenshot or export |
| `outputs/illustrative-siem/sample_alerts.csv` | Synthetic data | Example SIEM rows for learning and dashboard design |
