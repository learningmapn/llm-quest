# Level 7 — Fine-tuning

Notebooks corresponding to `llm-quest-theory/level-7/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-7--fine-tuning).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 7-1 | Supervised Fine-Tuning | [`7-1-sft.ipynb`](7-1-sft.ipynb) | ☑ |
| 7-2 | Preference Tuning (DPO) | [`7-2-preference.ipynb`](7-2-preference.ipynb) | ☑ |
| 7-3 | LoRA | [`7-3-lora.ipynb`](7-3-lora.ipynb) | ☑ |
| 7-4 | Safety & Red-teaming | [`7-4-safety.ipynb`](7-4-safety.ipynb) | ☑ |
| 7-5 | Fine-tune Boss (SQL Assistant) | [`7-5-finetune-boss.ipynb`](7-5-finetune-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly on CPU with `torch 2.2.2`, `transformers 4.46`, `peft 0.14`, `flan-t5-small/base`, `distilgpt2`, Python 3.10.

## Stack introduced in Level 7
- `peft>=0.10` — LoRA / PeftModel / adapter save/load/hot-swap
- `sqlite3` — the SQL sandbox for the Boss's execution-match metric
- (inherited from L5–6) `transformers`, `sentence-transformers`, `torch`

## First-run downloads
| Model | Size | Used in |
|---|---|---|
| `distilgpt2` | ~330 MB | 7-1, 7-2, 7-3 |
| `google/flan-t5-small` | ~80 MB | (alternative for 7-4) |
| `google/flan-t5-base` | ~250 MB | 7-4, 7-5 |

All cache to `~/.cache/huggingface/` (or `$HF_HOME`).

## Notes on runtime
- 7-1 through 7-3 each finish in 1–3 minutes on CPU (SFT/DPO/LoRA on `distilgpt2`).
- 7-4 runs ~1 minute (lots of `flan-t5-base` generations across the red-team suite).
- 7-5 trains LoRA on `flan-t5-base` for 12 epochs with 18 examples — roughly 3–6 minutes on CPU.

## About the Boss (7-5)
The source `.mdx` imagines an 8 B-parameter SQL Assistant shipped over FastAPI. To honour the project's CPU-only + no-paid-API rule, we keep every architectural idea (LoRA fine-tune, **execution-match** evaluation, destructive-query safety layer, before-vs-after benchmarking) and swap the model for `flan-t5-base`. Everything runs in a single notebook against an in-memory SQLite database. The mechanisms transfer to any larger model.

## Hot-swap demo in 7-3
The LoRA notebook shows how to load *two* adapters (reverse-and-uppercase vs uppercase-only) on a single base model, switch between them with `set_adapter()`, and serve them without re-loading the base. That is the deployment pattern real providers use.

## Run all in sequence
```bash
for nb in notebooks/level-7/7-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=1200
done

# Strip personal paths from execution outputs before committing.
python utils/scrub_notebooks.py
```
