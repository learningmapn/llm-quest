# Level 6 — Prompting, RAG, and Evaluation

Notebooks corresponding to `llm-quest-theory/level-6/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-6--prompting-rag-eval).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 6-1 | Prompt Patterns | [`6-1-prompt-patterns.ipynb`](6-1-prompt-patterns.ipynb) | ☑ |
| 6-2 | Few-Shot & Chain-of-Thought | [`6-2-few-shot-cot.ipynb`](6-2-few-shot-cot.ipynb) | ☑ |
| 6-3 | RAG — Indexing | [`6-3-rag-indexing.ipynb`](6-3-rag-indexing.ipynb) | ☑ |
| 6-4 | RAG — Retrieval | [`6-4-rag-retrieval.ipynb`](6-4-rag-retrieval.ipynb) | ☑ |
| 6-5 | LLM Evaluation | [`6-5-llm-eval.ipynb`](6-5-llm-eval.ipynb) | ☑ |
| 6-6 | Doc Assistant Boss | [`6-6-doc-assistant-boss.ipynb`](6-6-doc-assistant-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 6 notebooks execute cleanly on CPU with `torch 2.2.2`, `transformers 4.46`, `sentence-transformers 2.7`, `rank_bm25 0.2`, Python 3.10.

## Stack introduced in Level 6
- `google/flan-t5-small` and `google/flan-t5-base` — instruction-tuned encoder-decoder LMs, CPU-friendly (6-1, 6-2, 6-4, 6-5, 6-6)
- `sentence-transformers/all-MiniLM-L6-v2` — sentence embedder, reused from Level 5 (6-3, 6-4, 6-6)
- `rank_bm25.BM25Okapi` — pure-Python sparse retriever for hybrid search (6-4, 6-6)
- `sqlite3` in-memory — audit log for the Doc Assistant (6-6)

## About the vector index
The curriculum originally listed `faiss-cpu` as the index library. On Apple Silicon, installing `faiss-cpu` currently requires conda/MKL gymnastics that break in this project's `mlenv`. For the corpus sizes in these lessons (fewer than 100 chunks), a NumPy brute-force `embs @ q` is both faster in wall-clock time than FAISS's overhead and fully transparent for teaching. We call this out explicitly inside notebook 6-3, with a reflection question on when FAISS / HNSW actually becomes necessary. The same notebook's on-disk format (`embeddings.npy` + `chunks.jsonl`) is trivially portable to FAISS or Qdrant when needed.

## Pipeline between notebooks
Notebooks **6-3 → 6-4 → 6-6** share a persisted index at `$LLM_QUEST_DATA/rag_index` (default `/tmp/data/rag_index`). Run them in order the first time; on later runs the index is reused.

## First-run downloads
| Model | Size | Used in |
|---|---|---|
| `google/flan-t5-small` | ~80 M params | 6-1 |
| `google/flan-t5-base` | ~250 M params | 6-2, 6-4, 6-5, 6-6 |
| `all-MiniLM-L6-v2` | ~90 MB | 6-3, 6-4, 6-6 (shared with Level 5) |

All cache to `~/.cache/huggingface/`. Offline after the first run.

## Notes on runtime
- 6-1 and 6-3 finish in seconds.
- 6-2 and 6-5 need ~1–2 minutes each because they call the judge model many times.
- 6-4 and 6-6 need ~2–3 minutes each (full RAG + eval loop).

## About Boss 6-6
The theory describes a full-stack product with FastAPI, React, Qdrant and cloud LLMs. To honour the project rule of no paid APIs / no credentials, Boss 6-6 keeps the **architectural** pieces (hybrid retrieval, grounded prompt, strict refusal, citation check, SQLite audit log, category-stratified eval) and runs them locally. Porting to a hosted stack is an exercise; the interesting mechanisms are all here.

## Run all in sequence
```bash
for nb in notebooks/level-6/6-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=900
done

# Optional: dọn đường dẫn cá nhân khỏi outputs
python utils/scrub_notebooks.py
```
