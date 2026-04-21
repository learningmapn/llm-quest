# Level 8 — Agents

Notebooks corresponding to `llm-quest-theory/level-8/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-8--agents).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 8-1 | Planner / Executor | [`8-1-planner-executor.ipynb`](8-1-planner-executor.ipynb) | ☑ |
| 8-2 | Tool Calling | [`8-2-tool-calling.ipynb`](8-2-tool-calling.ipynb) | ☑ |
| 8-3 | Memory | [`8-3-memory.ipynb`](8-3-memory.ipynb) | ☑ |
| 8-4 | Multi-agent | [`8-4-multi-agent.ipynb`](8-4-multi-agent.ipynb) | ☑ |
| 8-5 | Research Boss | [`8-5-research-boss.ipynb`](8-5-research-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly on CPU with `torch 2.2.2`, `transformers 4.46`, `sentence-transformers 2.7`, `pydantic 2.13`, Python 3.10.

## Stack introduced in Level 8
- `pydantic>=2` — tool argument schemas + JSON schema generation + validation (8-2)
- `sentence-transformers` (reused) — vector long-term memory (8-3), research retriever (8-5)
- `google/flan-t5-base` (reused) — role-conditioned agents (8-4, 8-5)
- `concurrent.futures` stdlib — parallel tool calls (8-2)
- `sqlite3` is not used here; it returns in Level 9

## Mocking discipline
Notebooks 8-1 and 8-2 use a **deterministic MockLLM** (rule-based / hand-crafted outputs) so agent loops are reproducible without a paid API. Notebooks 8-3, 8-4, and 8-5 call `flan-t5-base` directly — the model is weak enough that the notebooks highlight its failure modes *and* the guardrails that rescue them (citation tagging, per-user memory isolation, refusal phrases).

## First-run downloads
- `google/flan-t5-base` (~250 MB) — inherited from Level 6
- `all-MiniLM-L6-v2` (~90 MB) — inherited from Level 5–6
No new model downloads.

## Notes on runtime
- 8-1, 8-2: seconds (CPU, no model call in 8-1; small flan-t5 calls in 8-2's examples).
- 8-3: ~30 seconds (mostly sentence-transformer embeddings).
- 8-4: ~1 minute (multi-role pipeline + debate + orchestrator).
- 8-5: ~2 minutes (plan + read + write across 4 eval questions + demo).

## What about the theory's web-search Research Boss?
The source `.mdx` builds around Tavily/SerpAPI. Per the project's no-paid-API rule, Boss 8-5 swaps the web for a **pre-loaded 5-passage corpus** (reusing the sentence-transformer retriever from Level 6). The Planner/Reader/Writer/Critic architecture, citation system, and rubric are all identical to the theory.

## Run all in sequence
```bash
for nb in notebooks/level-8/8-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=900
done
python utils/scrub_notebooks.py
```
