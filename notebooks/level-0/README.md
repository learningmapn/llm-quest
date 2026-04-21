# Level 0 — Math & Model Thinking

Notebooks corresponding to `llm-quest-theory/level-0/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-0--toán--tư-duy-mô-hình).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 0-1 | Variables & Functions | [`0-1-variables-functions.ipynb`](0-1-variables-functions.ipynb) | ☑ |
| 0-2 | Linear Model | [`0-2-linear-model.ipynb`](0-2-linear-model.ipynb) | ☑ |
| 0-3 | Vectors | [`0-3-vectors.ipynb`](0-3-vectors.ipynb) | ☑ |
| 0-4 | Matrices | [`0-4-matrices.ipynb`](0-4-matrices.ipynb) | ☑ |
| 0-5 | Derivatives | [`0-5-derivatives.ipynb`](0-5-derivatives.ipynb) | ☑ |
| 0-6 | House Price Boss | [`0-6-house-price-boss.ipynb`](0-6-house-price-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 6 notebooks execute cleanly under `jupyter nbconvert --execute` on `numpy 2.4`, `matplotlib 3.10`.

## Stack used in Level 0
`numpy`, `matplotlib`, `scipy` (optional), `sympy` (optional), `scikit-learn` (cross-check in the 0-6 boss).

## Run all in sequence
```bash
for nb in notebooks/level-0/0-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=120
done
```
