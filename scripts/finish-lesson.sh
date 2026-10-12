#!/bin/sh
# Finish a lesson: commit everything and push.
# Usage: scripts/finish-lesson.sh "0003 readonly-vs-write complete"
set -eu
git add -A
if git diff --cached --quiet; then
  echo "nothing to commit"
  exit 0
fi
git commit -m "${1:-lesson progress}"
git push
