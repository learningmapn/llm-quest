# Level 1 — Loss, Gradient Descent, Probability

Notebooks corresponding to `llm-quest-theory/level-1/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-1--loss-gradient-descent-xác-suất).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 1-1 | Loss Function | [`1-1-loss-function.ipynb`](1-1-loss-function.ipynb) | ☑ |
| 1-2 | Gradient Descent | [`1-2-gradient-descent.ipynb`](1-2-gradient-descent.ipynb) | ☑ |
| 1-3 | Learning Rate | [`1-3-learning-rate.ipynb`](1-3-learning-rate.ipynb) | ☑ |
| 1-4 | Probability | [`1-4-probability.ipynb`](1-4-probability.ipynb) | ☑ |
| 1-5 | Tune Boss | [`1-5-tune-boss.ipynb`](1-5-tune-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly under `jupyter nbconvert --execute` on `numpy 2.4`, `matplotlib 3.10`.

## Stack used in Level 1
`numpy`, `matplotlib` only. No torch yet — everything is hand-written so the mechanics stay visible.

## Run all in sequence
```bash
for nb in notebooks/level-1/1-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=180
done
```
