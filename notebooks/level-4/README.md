# Level 4 — Attention & Transformer Fundamentals

Notebooks corresponding to `llm-quest-theory/level-4/`. See details in
[../../docs/CURRICULUM.md](../../docs/CURRICULUM.md#level-4--attention--transformer-nguyên-lý).

| # | Lesson | Notebook | Status |
|---|---|---|---|
| 4-1 | RNN & Context Barrier | [`4-1-rnn-context.ipynb`](4-1-rnn-context.ipynb) | ☑ |
| 4-2 | Self-Attention | [`4-2-self-attention.ipynb`](4-2-self-attention.ipynb) | ☑ |
| 4-3 | Positional Encoding | [`4-3-positional-encoding.ipynb`](4-3-positional-encoding.ipynb) | ☑ |
| 4-4 | Multi-Head Attention | [`4-4-multi-head.ipynb`](4-4-multi-head.ipynb) | ☑ |
| 4-5 | Attention Boss (mini-GPT) | [`4-5-attention-boss.ipynb`](4-5-attention-boss.ipynb) | ☑ |

Last updated: 2026-04-21 — all 5 notebooks execute cleanly on CPU with `torch 2.2.2`, `numpy 1.24`, Python 3.10.

## Stack used in Level 4
`torch`, `torch.nn`, `torch.nn.functional`. No new external dependencies beyond Level 3.

## Notes on runtime
- 4-1 through 4-4 finish in ~1 minute each on CPU.
- 4-5 trains a ~120 k-parameter mini-GPT for 800 steps (~1–2 minutes on CPU). Loss falls well below the uniform-chance baseline of `log(VOCAB)`.

## What is different from the theory's Boss 4-5?
The source `.mdx` suggests loading pretrained BERT/GPT-2 with `transformers` and visualizing their attention. The curriculum (see [CURRICULUM.md](../../docs/CURRICULUM.md)) specifies building a mini Transformer block and training a character-level LM. The notebook honors **both** the curriculum and the visualization theme: we stack the primitives from lessons 4-1 through 4-4 into a tiny GPT, train it on a small corpus, and then extract attention heatmaps exactly as the theory envisions — but from a model we built ourselves, no external weights needed.

## Run all in sequence
```bash
for nb in notebooks/level-4/4-*.ipynb; do
  jupyter nbconvert --to notebook --execute "$nb" \
    --output "$(basename $nb)" --ExecutePreprocessor.timeout=600
done
```
