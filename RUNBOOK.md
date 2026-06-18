# RUNBOOK — devops-assistant-agent

> AI DevOps Assistant Agent (RAG-powered, Google Cloud Agent Builder)
> Updated: 2026-06-15

## Quick Reference

| Item | Value |
|------|-------|
| Platform | Google Cloud Agent Builder |
| Stack | Python, Terraform, Ansible knowledge base |
| Model | Gemini |
| Type | RAG chatbot |

---

## Procedures

### 1. Update Knowledge Base

```bash
# Add new documents to the knowledge base
python ingest.py --source docs/
```

### 2. Deploy Agent

```bash
terraform apply
```

### 3. Test Agent

```bash
python test_agent.py --query "How to deploy FastAPI on k3s?"
```

### 4. Troubleshooting

| Symptom | Fix |
|---------|-----|
| Agent returns irrelevant answers | Re-index knowledge base, check chunking |
| Terraform apply fails | Verify GCP credentials, check quota |
| API quota exceeded | Check Google Cloud Console billing/quotas |

---

## Secrets & Security

- GCP service account key: stored outside repo
- Gemini API key: environment variable
- ห้าม commit: service account JSON, API keys

---

## Related Docs

- `README.md` — architecture and setup
