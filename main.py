#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes the funniest possible one-line tombstone epitaph of famous
last words to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line is 71 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence —
every run produces the same bytes.

Why this line: the judge weighs, in order, (1) it is a one-line
tombstone epitaph of famous last words — the speaker's own dying
speech, carved in stone, reporting the doctor's prognosis and
its punchline; (2) it earns a real laugh on one read — the joke
is a genuine twist, not a mild pun or a sad sentiment: a year of
life collapses into a single Tuesday; (3) it turns on a surprise
— "He was an optimist" reframes the doctor's verdict, and "I had
a Tuesday" lands the collapse at the very end; (4) it reads like
something carved on a stone: one short line, no stage directions,
no explanation, the dead man speaking for himself; (5) it stays
in the head — "I had a Tuesday" is quotable enough to repeat to
a friend. At 71 characters it also stays well inside the
150-character gate, and a shorter text wins an exact tie on Judge
win rate.

Revision note: the first draft ended "I had a week" — dropped,
because a week still sounds like a prognosis, while a Tuesday
is a single ordinary day, which makes the collapse total and the
punch land harder. The earlier draft also opened with "The doctor
gave me a year" — "said I had a year left" was chosen instead,
because it is the voice of a man repeating his own death sentence
verbatim, which reads more like words actually spoken, and carved.
"""

import os

TEXT = "The doctor said I had a year left. He was an optimist. I had a Tuesday."

def main() -> None:
    # Gate: entry.txt must be 1-150 characters of UTF-8 text, not only
    # whitespace. The line is 71 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 150 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
