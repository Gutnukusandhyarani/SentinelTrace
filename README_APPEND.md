## SOC detection engineering and AI-assisted triage extension

This repository also includes a SOC detection-engineering extension covering five lab use cases: authentication abuse, local account creation, encoded PowerShell, scheduled-task creation, and suspicious LSASS process access. The extension contains Splunk SPL, Microsoft Sentinel KQL, Sigma YAML, MITRE ATT&CK mappings, false-positive tuning, L1 triage steps, three synthetic investigation walkthroughs, and three response playbooks.

The Python triage-copilot prototype extracts common IOC patterns, validates a strict JSON suggestion schema, supports a deterministic mock provider for repeatable software tests, and includes an optional local Ollama adapter. Human review is required; it does not perform containment.

**Evidence note:** SIEM query examples and the dashboard preview are illustrative, not exports from a connected SIEM. The included synthetic mock evaluation tests deterministic routing and schema behavior; it is not an LLM accuracy score. See `docs/execution-results.md` and `outputs/evidence-index.md`.

## Interactive SOC dashboard

A static, responsive, interactive dashboard is available in `dashboards/`. It reads the repository's own data files: illustrative SIEM alerts, mock copilot suggestions, evaluation summary, and the original SSH sample log. It includes alert search and filters, copilot case inspection, an SSH event timeline, a record detail drawer, and CSV export. It has no backend or API-key requirement.

Run locally from the repository root with `py -m http.server 8000`, then open `http://localhost:8000/dashboards/`. For public access, enable GitHub Pages from the repository's default branch and root folder. Full setup and source-data details are in `docs/dashboard-guide.md`.

**Dashboard evidence note:** visual totals are derived from the files loaded by the browser. SIEM examples remain illustrative; mock copilot fixture-match counts are not an LLM accuracy score. The dashboard is not connected to a live SIEM.
