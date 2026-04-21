# Level 2 — Regression & Model Evaluation

Notebooks corresponding to `llm-quest-theory/level-2/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-2--regression--đánh-giá-mô-hình).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 2-1 | Linear Regression | [`2-1-linear-regression.ipynb`](2-1-linear-regression.ipynb) | ☑ |
| 2-2 | Logistic Regression | [`2-2-logistic-regression.ipynb`](2-2-logistic-regression.ipynb) | ☑ |
| 2-3 | Train / Val / Test | [`2-3-train-val-test.ipynb`](2-3-train-val-test.ipynb) | ☑ |
| 2-4 | Bias vs Variance | [`2-4-bias-variance.ipynb`](2-4-bias-variance.ipynb) | ☑ |
| 2-5 | Churn Boss | [`2-5-churn-boss.ipynb`](2-5-churn-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly under `jupyter nbconvert --execute` on `numpy 2.4`, `matplotlib 3.10`, `scikit-learn` ≥ 1.4.

## Stack used in Level 2
`numpy`, `matplotlib`, `pandas` (2-5 only), `scikit-learn` (datasets, pipelines, metrics). Still no torch.

## Run all in sequence
```bash
for nb in notebooks/level-2/2-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=300
done
```
