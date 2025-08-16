#!/usr/bin/env bash
set -euo pipefail

readarray -t MARKDOWN_ARRAY < <(git ls-files '*.md')
prettier --write "${MARKDOWN_ARRAY[@]}"
codespell "${MARKDOWN_ARRAY[@]}"

readarray -t HTML_ARRAY < <(git ls-files '*.html')
djlint "${HTML_ARRAY[@]}"

uv pip compile pyproject.toml -o requirements.txt
