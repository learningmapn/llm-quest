# Level 3 — Neural Networks

Notebooks corresponding to `llm-quest-theory/level-3/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-3--neural-networks).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 3-1 | Neuron | [`3-1-neuron.ipynb`](3-1-neuron.ipynb) | ☑ |
| 3-2 | MLP | [`3-2-mlp.ipynb`](3-2-mlp.ipynb) | ☑ |
| 3-3 | Backpropagation | [`3-3-backprop.ipynb`](3-3-backprop.ipynb) | ☑ |
| 3-4 | Regularization | [`3-4-regularization.ipynb`](3-4-regularization.ipynb) | ☑ |
| 3-5 | Image Classifier Boss | [`3-5-image-classifier-boss.ipynb`](3-5-image-classifier-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly on CPU with `torch 2.2.2`, `numpy 1.24`, Python 3.10.

## Stack introduced in Level 3
`torch`, `torch.nn`, `torch.utils.data`, `torchvision.datasets.MNIST`. Everything runs on CPU; `DEVICE = "cpu"` is enforced.

## Notes on runtime
- 3-1 through 3-4: each finishes in under 30 seconds.
- 3-5 trains an MLP on 55k MNIST samples for 4 epochs (≈ 1–2 minutes on CPU). MNIST is cached at `/tmp/data` by default; override with `LLM_QUEST_DATA=/some/other/dir`.
- A CNN stretch cell in 3-5 is gated by `RUN_CNN = False` to keep the default run CPU-fast.

## Run all in sequence
```bash
for nb in notebooks/level-3/3-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=600
done
```
