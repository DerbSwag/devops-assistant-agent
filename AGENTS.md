# AGENTS.md

## Project Overview

AI DevOps Assistant Agent — RAG-powered chatbot built on Google Cloud Agent Builder (Vertex AI). Uses Terraform, Ansible, and LLMOps knowledge base to answer DevOps questions with grounded responses.

## Tech Stack

- Google Cloud Agent Builder — agent platform
- Gemini 2.5 Pro — LLM model
- Vertex AI Search — data store (RAG grounding)
- Python — API integration examples
- Shell (Bash) — knowledge base upload scripts
- GitHub Actions — CI (markdown lint + structure validation)

## Architecture

```
docs/
  agent-instructions.md   → System prompt / agent instructions
  architecture.md         → Detailed architecture documentation
examples/
  query_agent.py          → Python API integration example
knowledge-base/           → 28 files for Data Store (RAG source)
  llmops-*.md/txt         → LLMOps platform knowledge
  ansible-*.txt           → Ansible playbook knowledge
  terraform-*.txt         → Terraform IaC knowledge
scripts/
  upload-kb.sh            → Upload knowledge base to GCS
.github/workflows/ci.yml  → CI pipeline
.markdownlint.json        → Markdown lint config
```

## Conventions

- Knowledge base files: plain text (.txt) or markdown (.md)
- File naming: `{source}-{topic}.{ext}` (e.g., `ansible-docker-setup.txt`)
- Markdown follows `.markdownlint.json` rules
- Agent instructions maintained in `docs/agent-instructions.md`
- Default branch: `master`

## Commands

- Upload KB to GCS: `bash scripts/upload-kb.sh`
- Lint markdown: checked via CI
- Test agent: use Agent Builder Preview mode

## Important Notes

- Knowledge base sources: llmops-platform-lab, ansible-playbooks, aws-terraform-lab
- Data Store type: Unstructured documents on Cloud Storage
- Agent has Google Search as fallback tool
- Uses GenAI App Builder trial credits
