# Architecture

## Overview

DevOps Assistant Agent uses Google Cloud Agent Builder with Vertex AI Search (RAG) to provide grounded answers from real DevOps code and documentation.

## Components

| Component | Service | Details |
|-----------|---------|---------|
| Agent Runtime | Agent Builder Studio | Gemini 2.5 Pro model |
| Knowledge Base | Vertex AI Search | Unstructured document Data Store |
| Storage | Cloud Storage | `gs://devops-agent-kb/` (us-central1) |
| Search Fallback | Google Search | For questions outside knowledge base |

## Data Flow

1. User sends question via Preview/API
2. Agent receives query and determines if Data Store search is needed
3. VertexAISearchAgent retrieves relevant documents from Data Store
4. Agent generates response grounded in retrieved documents
5. If no relevant docs found, falls back to Google Search or general knowledge

## Agent Configuration

- **Agent ID**: `agent_1778502370266`
- **Data Store ID**: `devops-knowledge-base_1778501553350`
- **Project**: `zoneloop-automation`
- **Location**: `global`

## Knowledge Base Stats

- **Total files**: 28
- **Total size**: ~56.6 KB
- **Sources**: 3 GitHub repositories
- **Document types**: .md, .txt (converted from .py, .tf, .yml, .sh, .j2)
