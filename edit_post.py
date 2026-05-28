#!/usr/bin/env python3

import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CONTENT_PATH = Path(__file__).parent / "content"


def find_most_recent_file() -> tuple[Path, int]:
    pattern = str(CONTENT_PATH / "[0-9][0-9][0-9][0-9][0-9][0-9].md")
    existing_files = glob.glob(pattern)
    assert existing_files

    best_num = -1
    best_path = None
    for filepath in existing_files:
        filename = os.path.basename(filepath)
        match = re.match(r"^(\d{6})\.md$", filename)
        if match:
            n = int(match.group(1))
            if n > best_num:
                best_num = n
                best_path = Path(filepath)

    assert best_path is not None
    return best_path, best_num


def parse_post(filepath: Path) -> tuple[str, str]:
    """Return (header_block, body) where header_block includes the +++ delimiters."""
    text = filepath.read_text()
    # TOML front matter: +++\n...\n+++\n
    match = re.match(r"^(\+\+\+\n.*?\n\+\+\+\n)", text, re.DOTALL)
    assert match, f"Could not parse front matter in {filepath}"
    header = match.group(1)
    body = text[match.end() :]
    return header, body


def launch_editor(filepath: Path):
    try:
        subprocess.run(["nvim", str(filepath)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching editor: {e}")
        sys.exit(1)


def main():
    filepath, post_num = find_most_recent_file()
    print(f"Editing post #{post_num}: {filepath}")

    header, body_before = parse_post(filepath)

    launch_editor(filepath)

    _, body_after = parse_post(filepath)

    if body_after == body_before:
        print("No changes detected, skipping latest.json update.")
        sys.exit(0)

    with open("latest.json", "w") as f:
        data = {"number": post_num, "body": body_after.strip(), "sent": False}
        json.dump(data, f, indent=2)

    print("Updated latest.json")


if __name__ == "__main__":
    main()
