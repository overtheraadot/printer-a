#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

The office printer speaks at last: a tired veteran of twenty years,
four managers and nine hundred paper jams, answering everyone who
thumps it like the next jam is its fault. One line, written to
/output/entry.txt.
"""

import os

LINE = (
    "Twenty years, four managers, nine hundred paper jams — and you "
    "still thump me like the next one's my fault."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
