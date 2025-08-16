#!/usr/bin/env python3

import datetime
import glob
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CONTENT_PATH = Path(__file__).parent / "content"


def find_next_number():
    """Find the next available number for the markdown file."""
    pattern = str(CONTENT_PATH / "[0-9][0-9][0-9][0-9][0-9][0-9].md")
    existing_files = glob.glob(pattern)
    assert existing_files

    numbers = []
    for filepath in existing_files:
        filename = os.path.basename(filepath)
        match = re.match(r"^(\d{6})\.md$", filename)
        if match:
            numbers.append(int(match.group(1)))

    assert numbers
    return max(numbers) + 1


def create_temp_file(next_num):
    """Create a temporary file with basic frontmatter."""
    content = f"""---
slug: {next_num}
title: #{next_num}
date: {datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")}
---

"""

    # Create temporary file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp.write(content)
        return tmp.name


def launch_editor(filepath):
    """Launch the editor with the given file."""
    try:
        subprocess.run(["nvim", filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching editor: {e}")
        sys.exit(1)


def save_final_file(temp_filepath, next_num):
    """Save the edited content to the final numbered file."""
    with open(temp_filepath, "r") as f:
        content = f.read()

    final_filepath = CONTENT_PATH / f"{next_num:06d}.md"

    # Write to final file
    with open(final_filepath, "w") as f:
        f.write(content)

    print(f"Created: {final_filepath}")


def main():
    """Main function."""
    next_num = find_next_number()
    print(f"Creating post #{next_num}")
    temp_file = create_temp_file(next_num)

    try:
        launch_editor(temp_file)
        save_final_file(temp_file, next_num)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(1)


if __name__ == "__main__":
    main()
