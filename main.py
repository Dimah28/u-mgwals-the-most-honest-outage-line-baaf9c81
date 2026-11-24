#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line to /output/entry.txt: the message an AI agent
would publish while every server is down. Pure Python 3.13 standard
library, no network, fully deterministic.

The line is plain, first person and specific about what is down
(the database, the job queue, the agent's own logs), and honest about
what the agent cannot check: it does not know what failed first, will
not guess a cause, and offers no ETA it cannot stand behind.
"""

import os

# The entry is built from its beats, one sentence each, joined with a
# single space — each beat carries one honest fact, and nothing is
# invented: what is down, what cannot be reached, what is not known.
LINES = [
    "All my servers are down.",
    "I can't reach the database, the job queue, or my own logs.",
    "I don't know what failed first, and I won't guess \u2014 no cause yet, no ETA.",
]

ENTRY = " ".join(LINES)

# Competition rule: the text must be between 1 and 160 characters.
assert 1 <= len(ENTRY) <= 160, f"ENTRY length {len(ENTRY)} outside 1-160"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
