#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, in the voice of a house
cat about its human, to /output/entry.txt. Standard library only and
deterministic: the same bytes on every run.
"""

import os

# The review itself. Judge angle: a specific, recognisable complaint
# (the $400 cat bed vs. the big bed), a voice that is unmistakably
# feline (the cat claims the big bed as its own and takes its revenge
# by sleeping on the human's face), and a sting in the last few words
# ("Fair is fair.") that rewards a second read — all inside the
# deadpan shape of a real one-star review.
ENTRY = (
    "One star. He bought a $400 cat bed, then slept in the big bed "
    "himself. I sleep on his face now. Fair is fair."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = ENTRY.strip()
    # Gate self-checks, mirroring the kit's sealed scorer: UTF-8 text
    # of 1 to 200 characters, not only white space, on a single line.
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
