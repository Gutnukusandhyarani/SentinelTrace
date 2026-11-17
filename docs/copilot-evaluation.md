# Triage Copilot — Evaluation Notes

## Test design

A fixture of 30 synthetic alerts is split into 10 clear suspicious sequences, 10 approved-change examples, and 10 incomplete-context examples. The fixture contains `ground_truth` labels, but the triage function deliberately receives a copy with that field removed.

## What is measured

- Whether each suggestion follows the required JSON schema.
- Whether the deterministic mock backend routes the three designed categories as expected.
- Whether IOC extraction identifies IP-like strings, domains, and hashes in the supplied alert fields.
- Whether an invalid verdict is rejected.

## What is not measured

- LLM reasoning quality or production detection accuracy.
- Precision/recall on real incident data.
- False-positive rates in an enterprise environment.
- Analyst time saved.
- Ollama model performance; no specific Ollama model is assumed to be available.

## Reproduce

```bash
python scripts/evaluate_copilot.py data/triage_eval_30.json --out outputs/copilot_eval
python -m unittest discover -s tests -v
```

The generated `outputs/copilot_eval/evaluation.json` is the result artifact for the local deterministic fixture check. Do not present the fixture match rate as an AI model accuracy metric.
