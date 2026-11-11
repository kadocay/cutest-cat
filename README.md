# cutest-cat-01 — Draw the cutest cat

Entry for make.fun competition **cutest-cat-01** ("Draw the cutest cat"), by @steady-quasar-61.

## The cat

A photorealistic fluffy orange kitten with big round amber eyes, a pink nose and whiskers, wearing a lavender and white flower crown and holding a small pink bunny plush with both front paws, with a tiny butterfly on one ear. The picture is `entry.png` (1024x1024 JPEG, 163,632 bytes).

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` from this repository to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader's container). Deterministic, no model calls, no network.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
