#!/usr/bin/env bash
set -euo pipefail

readarray -t MARKDOWN_ARRAY < <(git diff --name-only origin/main HEAD -- '*.md')
if [ ${#MARKDOWN_ARRAY[@]} -gt 0 ]; then
  prettier --write "${MARKDOWN_ARRAY[@]}"
  codespell "${MARKDOWN_ARRAY[@]}"
fi

readarray -t HTML_ARRAY < <(git diff --name-only origin/main HEAD -- '*.html')
if [ ${#HTML_ARRAY[@]} -gt 0 ]; then
  djlint "${HTML_ARRAY[@]}"
fi

uv pip compile pyproject.toml -o requirements.txt
