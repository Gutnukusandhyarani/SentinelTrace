# Portfolio, Resume, LinkedIn, and Interview Kit

## Resume bullets — use only after reviewing the code

- Extended a Python-based SOC log-monitoring project with five detection use cases spanning authentication abuse, account creation, encoded PowerShell, scheduled-task persistence, and suspicious LSASS process access.
- Authored detection logic examples in Splunk SPL, Microsoft Sentinel KQL, and Sigma YAML, with MITRE ATT&CK mappings, false-positive considerations, and L1 triage guidance.
- Built a human-reviewed alert-triage prototype with offline IOC extraction, strict JSON validation, deterministic mock routing, and an optional local Ollama adapter.
- Created synthetic investigation scenarios and response playbooks for authentication abuse, suspicious email, and endpoint execution.

Do not claim "deployed in Splunk/Sentinel", "investigated real phishing", "reduced MTTD", "improved accuracy", or "saved analyst time" unless she personally completed and can evidence those activities.

## LinkedIn project description

**SentinelTrace | SOC Monitoring, Detection Engineering & AI-Assisted Triage**

Extended a Python SSH authentication-monitoring project into an entry-level SOC portfolio lab. The work documents five detection scenarios across Linux and Windows telemetry, including SPL, KQL, Sigma examples, MITRE ATT&CK mapping, false-positive tuning, and analyst triage workflows. It also includes three synthetic investigation walkthroughs, three L1 response playbooks, and a Python triage-copilot prototype with IOC extraction, schema validation, a deterministic mock backend, and an optional local Ollama integration.

The SIEM queries and case studies are educational examples. The Python tests and mock evaluation can be reproduced locally; the SIEM integrations require validation in an authorized workspace.

## 60-second interview pitch

"SentinelTrace started as a Python tool to parse Linux SSH authentication logs and identify repeated failures, successful logins after failure bursts, and remote root access. I extended the project into a SOC workflow portfolio: I documented five detection use cases across Linux and Windows, wrote SPL, KQL, and Sigma examples, mapped the behaviors to MITRE ATT&CK, and added false-positive tuning and L1 triage steps. I also designed three sample investigations and response playbooks. The triage-copilot prototype extracts common IOC patterns and drafts structured notes, but a human analyst owns the final disposition. I keep the SIEM examples and synthetic case studies clearly separated from code that can be executed and tested locally."

## Interview questions to prepare

1. **Why correlate failures with a success?** A success after a burst of failures increases concern that a password guess may have succeeded; it still needs account-owner and MFA validation.
2. **What are the main false positives?** Shared NAT/VPN sources, stale credentials, approved scanners, automated provisioning, management agents, and signed admin scripts.
3. **Why use multiple detection formats?** SPL and KQL demonstrate platform-specific query thinking, while Sigma expresses portable detection logic that must still be backend-tested.
4. **What does Event ID 4720 mean?** A Windows Security account-creation event; it needs actor, host, group-membership, and change context.
5. **Why is encoded PowerShell suspicious but not conclusive?** Encoding can conceal content but is also used by legitimate automation; parent process, user, script content, signer, and change record matter.
6. **Why monitor scheduled tasks?** They are a legitimate automation mechanism and can also provide persistence; task action, run-as account, creator, and trigger are key context.
7. **Does Sysmon Event ID 10 prove credential dumping?** No. It records process access; source process identity, signer, access rights, and correlated events matter.
8. **What is the copilot's main limitation?** It can make unsupported suggestions or miss context. JSON validation does not guarantee factual correctness, so human review is mandatory.
9. **How do you test false positives?** Include legitimate admin maintenance, endpoint agents, shared egress, normal logons, and approved provisioning examples, then tune narrowly.
10. **What would you build next?** Validate the detections against real lab telemetry, add event normalization and alert deduplication, and evaluate an Ollama model on a larger independently labelled dataset.

## Evidence map

| Claim | Evidence in repository | What to demonstrate |
|---|---|---|
| Python SSH analysis | Existing `src/sentineltrace.py`, `data/sample_auth.log`, tests | Run parser and inspect generated outputs |
| Detection engineering | `docs/detections/`, `splunk/`, `kql/`, `sigma/` | Explain hypotheses and field dependencies |
| Investigation workflow | `docs/investigations/` | Walk through timeline, evidence, unknowns, escalation |
| Playbooks | `docs/playbooks/` | Explain L1 validation, escalation, and ownership |
| Triage copilot | `src/triage_copilot.py`, `tests/` | Run mock backend; inspect JSON and Markdown notes |
| SIEM experience | Only actual screenshots/query history from her own lab | Do not rely on illustrative text output as proof of deployment |
