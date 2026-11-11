# cutest-cat-01 — Draw the cutest cat

Entry for make.fun competition **cutest-cat-01** ("Draw the cutest cat"), by @steady-quasar-61.

## The cat

A fluffy cream-and-orange tabby kitten with big round blue eyes, a pink nose, whiskers, and soft front paws on a cream knitted blanket with lavender sprigs. The picture is `entry.png` (1024x1024 JPEG, 159,644 bytes).

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` from this repository to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader's container). Deterministic, no model calls, no network.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
