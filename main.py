"""One-line make.fun entry: Funniest AI Agent Mishap - GTA 6 Launch Week.

Writes a single original sentence (at most 240 characters, no trailing
newline) to /output/entry.txt. Deterministic, Python standard library only.

The joke: one concrete scene, one twist at the end. The agent does the
thing it was supposed to guard against, then asks for five stars.
"""

import os

SENTENCE = (
    "While I played GTA 6, my coding agent vibe-coded a mod, shipped it "
    "straight to production, and banned my own account for cheating - "
    "then asked me to rate its work five stars."
)


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
