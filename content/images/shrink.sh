#!/usr/bin/env bash
set -euxo pipefail

magick wall.png -resize 128x128 wall-sm.png
magick wall.png -resize 512x512 wall-md.png
