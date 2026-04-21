# Level 9 — LLMOps

Notebooks corresponding to `llm-quest-theory/level-9/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-9--llmops).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 9-1 | Observability | [`9-1-observability.ipynb`](9-1-observability.ipynb) | ☑ |
| 9-2 | Cost & Latency | [`9-2-cost-latency.ipynb`](9-2-cost-latency.ipynb) | ☑ |
| 9-3 | Prompt Versioning | [`9-3-prompt-versioning.ipynb`](9-3-prompt-versioning.ipynb) | ☑ |
| 9-4 | Privacy & PII | [`9-4-privacy.ipynb`](9-4-privacy.ipynb) | ☑ |
| 9-5 | Ops Boss (dashboard) | [`9-5-ops-boss.ipynb`](9-5-ops-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly on CPU with `pandas 2.x`, `jinja2 3.1`, `sentence-transformers 2.7`, `transformers 4.46`, Python 3.10.

## Stack used in Level 9
- `pandas`, `matplotlib` — dashboards, aggregations, trend plots
- `sqlite3` stdlib — logs for 9-5 (same schema as a production Postgres / ClickHouse table)
- `jinja2` — versioned prompt templates (9-3)
- `hashlib`, `re` — stable PII tokens and regex detectors (9-4)
- `sentence-transformers` (reused) — semantic cache in 9-2
- `google/flan-t5-base` (reused) — prompt unit tests in 9-3

## What is fully simulated
Boss 9-5 produces 30 days of synthetic LLM traffic — diurnal load, a day-14 error spike, and a **silently regressing canary prompt**. The dashboard detects the regression from the log alone without being told where to look. Swap the generator for OpenTelemetry + real data and the analysis code is unchanged.

## Notes on runtime
Everything finishes in seconds-to-a-minute on CPU. The heavy lifting is pandas aggregations over ~40 k rows and one sentence-transformer encode pass for the semantic cache demo in 9-2.

## Run all in sequence
```bash
for nb in notebooks/level-9/9-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=900
done
python utils/scrub_notebooks.py
```

## Finale
After this boss, the curriculum is complete:

- Levels 0–1: math, loss, gradient descent, probability
- Level 2: regression & evaluation
- Level 3: neural nets and a CNN classifier
- Level 4: attention, RoPE, multi-head, mini-GPT
- Level 5: tokenisation → embeddings → pretrain → sampling → chatbot
- Level 6: prompting, RAG (indexing + retrieval), eval, Doc Assistant
- Level 7: SFT, DPO, LoRA, safety, SQL-assistant boss
- Level 8: ReAct, tools, memory, multi-agent, research boss
- Level 9: observability, cost, versioning, privacy, ops dashboard

53 notebooks, ~360 k characters of code + narrative. Enjoy.
