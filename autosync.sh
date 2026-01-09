#!/bin/bash
cd "$(dirname "$0")"
while inotifywait -r -e modify,create,delete,move .; do
    git add .
    git commit -m "Auto update $(date '+%Y-%m-%d %H:%M:%S')" || true
    git push origin main
done
