## SOC detection engineering and AI-assisted triage extension

This repository also includes a SOC detection-engineering extension covering five lab use cases: authentication abuse, local account creation, encoded PowerShell, scheduled-task creation, and suspicious LSASS process access. The extension contains Splunk SPL, Microsoft Sentinel KQL, Sigma YAML, MITRE ATT&CK mappings, false-positive tuning, L1 triage steps, three synthetic investigation walkthroughs, and three response playbooks.

The Python triage-copilot prototype extracts common IOC patterns, validates a strict JSON suggestion schema, supports a deterministic mock provider for repeatable software tests, and includes an optional local Ollama adapter. Human review is required; it does not perform containment.

**Evidence note:** SIEM query examples and the dashboard preview are illustrative, not exports from a connected SIEM. The included synthetic mock evaluation tests deterministic routing and schema behavior; it is not an LLM accuracy score. See `docs/execution-results.md` and `outputs/evidence-index.md`.
