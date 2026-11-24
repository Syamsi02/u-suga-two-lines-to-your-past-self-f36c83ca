"""Two Lines to Your Past Self.

Writes the entry text -- exactly two lines -- to /output/entry.txt.

Line one warns the writer's past self about one specific moment, in a
single sentence. Line two says in one sentence why that moment mattered
and what changed because of it.

Pure Python standard library; deterministic: the same bytes every run.
"""

import os

LINE_1 = (
    "When Mrs Hart slides the art-school application across your desk "
    "and says 'you should apply', don't laugh and hand it back."
)

LINE_2 = (
    "That laugh costs you the only portfolio review that ever mattered, "
    "and you spend the next ten years drawing in notebooks no one ever sees."
)

ENTRY = LINE_1 + "\n" + LINE_2

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no line may be blank"
    for line in lines:
        # One sentence per line: a single terminal period, at the end.
        assert line.endswith("."), "each line must end its sentence"
        assert line.count(".") == 1, "each line must hold one sentence"
    assert 1 <= len(ENTRY) <= 280, "entry must be 1 to 280 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
