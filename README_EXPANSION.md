# SentinelTrace — SOC Portfolio Expansion Pack

This pack extends the existing SentinelTrace SSH log analyzer with analyst-focused documentation and a local triage-copilot example. It is designed to be merged into the existing `SentinelTrace` repository without replacing the original Python analyzer.

## Evidence labels used throughout

- **[VERIFIED IN THIS PACK]** — generated or tested by running the included code in this workspace.
- **[SYNTHETIC LAB DATA]** — fabricated, safe training events; not collected from a company, client, or live endpoint.
- **[ILLUSTRATIVE SIEM OUTPUT]** — representative Splunk / Microsoft Sentinel output showing what an analyst may see after ingesting equivalent lab events. These are not screenshots or exports from an installed SIEM instance.
- **[RUN IN YOUR SIEM]** — query examples; field names and data models may need adapting to the actual connector, index, table, and parser.

## What is included

```text
docs/
  detections/       Five L1 detection use cases and field requirements
  investigations/   Three worked example investigations
  playbooks/        Brute-force, phishing, and suspicious-execution response guides
  copilot/          Design, evaluation notes, limitations, and analyst templates
  references.md     Official ATT&CK, Microsoft, Sysmon, and Sigma references
splunk/              SPL examples
kql/                 Microsoft Sentinel KQL examples
sigma/               Sigma YAML rules
src/triage_copilot.py
data/triage_eval_30.json
tests/test_triage_copilot.py
scripts/evaluate_copilot.py
```

## Merge into the existing project

Copy the folders and files in this pack into the root of the existing `SentinelTrace` repository. When prompted, merge folders; do not delete or overwrite the original `src/sentineltrace.py`, `data/sample_auth.log`, or its tests.

## Run the copilot example

Python 3.10+; standard library only.

```bash
python src/triage_copilot.py data/triage_eval_30.json --backend mock --out outputs/copilot_demo
python scripts/evaluate_copilot.py data/triage_eval_30.json --out outputs/copilot_eval
python -m unittest discover -s tests -v
```

The mock backend is deterministic and useful for verifying plumbing, schema validation, IOC extraction, and audit logging. It is **not an LLM quality benchmark**. To connect an already-running local Ollama service:

```bash
python src/triage_copilot.py data/triage_eval_30.json --backend ollama --model YOUR_LOCAL_MODEL --out outputs/ollama_demo
```

This option requires Ollama to be running locally and the named model to be available. No model is downloaded by this project. Model-generated suggestions must be reviewed by a human analyst.

## Portfolio wording

Use wording such as:

> Extended SentinelTrace with a SOC detection engineering pack covering five authentication, account, PowerShell, scheduled-task, and credential-access use cases; documented SPL, KQL, Sigma logic, ATT&CK mappings, triage steps, and false-positive tuning. Built a human-reviewed Python triage-copilot prototype with offline IOC extraction, schema validation, a deterministic mock backend, and an optional local Ollama adapter.

Only say that Splunk or Sentinel detections were *deployed and tested* after the queries have actually been run in an authorized lab workspace. The examples here demonstrate detection design, not an actual SIEM deployment.
