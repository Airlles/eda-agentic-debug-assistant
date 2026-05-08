# AWS Deployment Guide

## Project

Cloud-Deployed AI Debug Assistant for FPGA and RTL Logs

## Purpose

This project exposes an AI-assisted FPGA and RTL log debugging workflow through a cloud-ready FastAPI API. The service accepts FPGA or RTL log text, classifies common design/debug issues, retrieves debug context from a Markdown knowledge base, and returns a structured Markdown report.

## System Overview

The project is organized into four layers:

1. `debug_knowledge.md` stores reusable debug guidance for common RTL and EDA issues.
2. `rag.py` retrieves the relevant debug context from the knowledge base.
3. `mcp_server.py` exposes parsing and retrieval tools through MCP.
4. `app.py` exposes the workflow through a FastAPI API.

## Local API Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
python -m uvicorn app:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Routes

```text
GET /
POST /debug
```

## Health Check

```bash
curl http://localhost:8000/
```

Expected response:

```json
{
  "status": "running",
  "service": "AI RTL Debug Assistant",
  "cloud_ready": true
}
```

## Debug Endpoint Example

```bash
curl -X POST http://localhost:8000/debug \
  -H "Content-Type: application/json" \
  -d "{\"log_text\": \"Warning: Width mismatch in assignment at alu.v line 24\nError: Port data_in expects 8 bits but connected signal has 4 bits\"}"
```

Expected issue classification:

```text
WIDTH_MISMATCH
```

## Docker Configuration

This project includes Docker configuration so the FastAPI service can be packaged as a containerized engineering tool.

Build image:

```bash
docker build -t ai-rtl-debug-assistant .
```

Run container:

```bash
docker run -p 8000:8000 ai-rtl-debug-assistant
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## AWS App Runner Deployment Flow

1. Build the Docker image locally.
2. Push the Docker image to Amazon Elastic Container Registry.
3. Create an AWS App Runner service using the ECR image.
4. Configure the service to expose port `8000`.
5. Test the public service URL using the `/` health check route.
6. Send FPGA or RTL log text to the `/debug` endpoint.
7. Verify that the service returns issue classification, extracted evidence, retrieved context, and a Markdown report.

## Custom Configuration

Future environment variables:

```text
LOG_CLASSIFIER_MODE=regex
REPORT_FORMAT=markdown
MAX_EVIDENCE_LINES=5
KNOWLEDGE_BASE_PATH=debug_knowledge.md
```

## Project Relevance

This project demonstrates:

1. AI workflow integration
2. Cloud-ready API deployment
3. Containerized engineering tooling
4. FPGA and RTL debug automation
5. Technical documentation
6. Knowledge base content
7. Internal and customer-facing report generation
8. Debugging discrepancies in hardware design logs