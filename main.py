"""Monday Morning Punchlines — entry writer.

The joke: Friday-you is an optimist who makes plans; Monday-you is the
detective who has to live with them. One line, written verbatim to
/output/entry.txt.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"
MAX_LINE_CHARS = 200  # contest cap for a one-line entry

# The entry is a two-beat joke: the setup (Friday me's optimism) and the
# tag (Monday me's revenge investigation). Keeping the beats separate makes
# it easy to retime the punch without touching the machinery below.
SETUP = "Friday me booked Monday me into a 7 a.m. spin class."
TAG = "Monday me showed up for one reason: to identify the traitor."


def build_line() -> str:
    """Assemble the single-line entry from its two beats."""
    return f"{SETUP} {TAG}"


def validate(line: str) -> str:
    """Return the line unchanged if it is a legal entry, else raise."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be empty")
    if len(line) > MAX_LINE_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_LINE_CHARS} cap")
    return line


def main() -> None:
    line = validate(build_line())
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
