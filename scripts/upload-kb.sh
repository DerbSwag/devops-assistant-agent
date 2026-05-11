#!/bin/bash
# Upload knowledge base files to Google Cloud Storage
# Usage: ./scripts/upload-kb.sh [bucket-name]

BUCKET="${1:-devops-agent-kb}"
KB_DIR="knowledge-base"

if [ ! -d "$KB_DIR" ]; then
  echo "ERROR: $KB_DIR/ directory not found"
  exit 1
fi

echo "Uploading $KB_DIR/ to gs://$BUCKET/ ..."
gsutil -m cp "$KB_DIR"/* "gs://$BUCKET/"
echo "✅ Done. Files uploaded to gs://$BUCKET/"
echo ""
echo "Next: Re-import data in Agent Builder Data Store to pick up changes."
