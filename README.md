# 🤖 DevOps Assistant Agent

AI-powered DevOps assistant built on **Google Cloud Agent Builder** — uses RAG (Retrieval-Augmented Generation) with Gemini 2.5 Pro to answer infrastructure questions grounded in real production code.

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Agent%20Builder-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/products/agent-builder)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Pro-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![RAG](https://img.shields.io/badge/RAG-Vertex%20AI%20Search-34A853?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/vertex-ai-search-and-conversation)

## Overview

This agent answers DevOps questions by searching a curated knowledge base of 28 files extracted from three production repositories. Unlike generic AI assistants, responses are **grounded in actual infrastructure code** — Terraform configs, Ansible playbooks, Docker Compose files, and monitoring setups.

### Capabilities

| Domain | What the Agent Can Do |
|--------|----------------------|
| **Terraform/AWS** | Explain VPC/EC2 configs, generate modules, suggest best practices |
| **Ansible** | Write playbooks, debug tasks, recommend hardening steps |
| **LLMOps/AI Infra** | Explain RAG pipelines, AI security, prompt guard, gateway routing |
| **Docker/Compose** | Service orchestration, networking, multi-container setups |
| **CI/CD** | GitHub Actions workflows, deployment strategies |
| **Monitoring** | Prometheus configs, Grafana dashboards, alerting rules |

## 📸 Demo

![DevOps Assistant Demo](assets/demo-screenshot.png)

![Agent Configuration](assets/agent-config.png)

![Deployment Success](assets/deployment-success.png)

## 🏗️ Architecture

```text
User (Chat)
    │
    ▼
Google Cloud Agent Builder Studio
    ├── Model: Gemini 2.5 Pro
    ├── Grounding: Vertex AI Search (RAG)
    └── Fallback: Google Search
    │
    ▼
Data Store (Knowledge Base — 28 files)
    ├── llmops-platform-lab/   → LLM Gateway, RAG, AI Security, Monitoring
    ├── ansible-playbooks/     → Docker, FastAPI, Monitoring, Hardening
    └── aws-terraform-lab/     → VPC, EC2, Security Groups, Terraform IaC
```

**Data Flow:** User sends query → Agent searches Data Store via Vertex AI Search → retrieves relevant docs → generates grounded response. Falls back to Google Search if no relevant documents found.

## 🚀 Quick Start

### Prerequisites

- Google Cloud account with billing enabled
- Agent Builder API activated
- `gcloud` CLI configured

### Deploy

```bash
# 1. Upload knowledge base to Cloud Storage
gsutil mb -l us-central1 gs://devops-agent-kb/
gsutil -m cp knowledge-base/* gs://devops-agent-kb/

# 2. Or use the upload script
./scripts/upload-kb.sh
```

Then in Google Cloud Console:

1. **Create Data Store** — [Agent Builder > Data Stores](https://console.cloud.google.com/gen-app-builder/data-stores) → Cloud Storage → `gs://devops-agent-kb/` → Unstructured documents
2. **Create Agent** — [Agent Platform Studio](https://console.cloud.google.com/gen-app-builder/agents) → Name: `DevOps Assistant` → paste instructions from [`docs/agent-instructions.md`](docs/agent-instructions.md) → connect Data Store
3. **Test** — Use Preview mode:

```text
"อธิบาย architecture ของ LLM Gateway"
"เขียน Ansible playbook สำหรับ install Docker"
"Terraform main.tf สร้าง resource อะไรบ้าง"
```

### API Integration

Use the Dialogflow CX API to query the agent programmatically:

```bash
pip install google-cloud-dialogflow-cx==1.35.0
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"
python examples/query_agent.py
```

See [`examples/query_agent.py`](examples/query_agent.py) for full implementation.

## 📁 Project Structure

```text
devops-assistant-agent/
├── knowledge-base/              # 28 RAG source files (.md, .txt)
│   ├── llmops-*                 #   LLM Gateway, RAG, Security, Monitoring
│   ├── ansible-*               #   Playbooks, templates, hardening
│   ├── terraform-*             #   AWS IaC configs
│   ├── fastapi-lab-*           #   FastAPI app, Docker, Nginx
│   ├── content-pipeline-*      #   Content automation pipeline
│   └── it-toolkit-*            #   IT helpdesk tools
├── docs/
│   ├── agent-instructions.md   # System prompt for the agent
│   └── architecture.md         # Detailed architecture documentation
├── examples/
│   └── query_agent.py          # Python API integration example
├── scripts/
│   └── upload-kb.sh            # Upload knowledge base to GCS
├── .github/workflows/ci.yml    # CI: markdown lint + structure validation
├── LICENSE                     # MIT
└── README.md
```

## 🔗 Knowledge Base Sources

| Repository | Content |
|-----------|---------|
| [llmops-platform-lab](https://github.com/DerbSwag/llmops-platform-lab) | LLM Gateway, RAG Pipeline, AI Security, Prometheus/Grafana |
| [ansible-playbooks](https://github.com/DerbSwag/ansible-playbooks) | Docker setup, FastAPI deploy, Monitoring, Server hardening |
| [aws-terraform-lab](https://github.com/DerbSwag/aws-terraform-lab) | AWS VPC, EC2, Security Groups, Terraform IaC |
| [fastapi-lab](https://github.com/DerbSwag/fastapi-lab) | FastAPI app, Docker, Nginx, Monitoring stack |
| [content-pipeline](https://github.com/DerbSwag/content-pipeline) | Content automation, VPS setup, Health checks |
| [it-toolkit](https://github.com/DerbSwag/it-toolkit) | IT helpdesk tools, GLPI Agent, PC info scripts |

## 💰 Cost Estimate

Uses Google Cloud GenAI App Builder with trial credits. Approximate costs:

| Component | Cost |
|-----------|------|
| Data Store indexing | Minimal (one-time) |
| Agent queries | ~$0.01–0.05 per query |
| Google Search grounding | Included in credits |

## 🎯 What This Project Demonstrates

- Building RAG-based AI agents on Google Cloud
- Document grounding with Vertex AI Search
- Integrating real DevOps code into conversational AI
- Production-grade agent design with structured instructions
- CI/CD pipeline for knowledge base validation

## 📄 License

[MIT](LICENSE)
