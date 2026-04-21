# Level 5 — Tokenization → Full LLM

Notebooks corresponding to `llm-quest-theory/level-5/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-5--tokenization--llm-hoàn-chỉnh).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 5-1 | Tokenization | [`5-1-tokenization.ipynb`](5-1-tokenization.ipynb) | ☑ |
| 5-2 | Embeddings | [`5-2-embedding.ipynb`](5-2-embedding.ipynb) | ☑ |
| 5-3 | Pretraining | [`5-3-pretraining.ipynb`](5-3-pretraining.ipynb) | ☑ |
| 5-4 | Transformer Architecture | [`5-4-transformer-arch.ipynb`](5-4-transformer-arch.ipynb) | ☑ |
| 5-5 | Sampling | [`5-5-sampling.ipynb`](5-5-sampling.ipynb) | ☑ |
| 5-6 | Chatbot Boss (local) | [`5-6-chatbot-boss.ipynb`](5-6-chatbot-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 6 notebooks execute cleanly on CPU with `torch 2.2.2`, `transformers 4.46`, `tokenizers 0.20`, `sentence-transformers 2.7`, Python 3.10.

## Stack introduced in Level 5
- `tokenizers` — train BPE from scratch (5-1)
- `transformers.AutoTokenizer` — pretrained GPT-2 tokenizer (5-1, 5-5, 5-6)
- `sentence-transformers/all-MiniLM-L6-v2` (~90 MB) — sentence embeddings (5-2)
- `distilgpt2` (~330 MB) — pretrained decoder-only LM (5-5 sampling, 5-6 chat)
- `sqlite3` — in-memory chat log (5-6)

## First-run downloads
| Model | Size | Used in |
|---|---|---|
| `gpt2` tokenizer | ~1 MB | 5-1 |
| `all-MiniLM-L6-v2` | ~90 MB | 5-2 |
| `distilgpt2` | ~330 MB | 5-5, 5-6 |

All stored in `~/.cache/huggingface/` by default. Once cached, each notebook runs offline.

## Notes on runtime
- 5-1 through 5-4: 10-30 seconds each on CPU.
- 5-5: ~1 minute (several generations with distilgpt2).
- 5-6: ~1-2 minutes (multi-turn generations at ~1-3 tokens/sec on CPU).

## Important: Boss 5-6 is *local*
The theory's boss assumes a paid Claude or OpenAI API. To honour the project rule of no paid APIs and no credentials, the notebook builds the same architecture (system prompt, history sliding window, guardrails, logging) around `distilgpt2`. The model itself is weak, but every infrastructure layer around it is real.

## Run all in sequence
```bash
for nb in notebooks/level-5/5-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=900
done
```
