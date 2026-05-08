## Cloud API and Containerization

This project includes a FastAPI wrapper that exposes the RTL and FPGA debug assistant as a cloud-ready API. The API accepts log text, classifies the likely issue type, retrieves debug context from the knowledge base, and returns a structured Markdown report.

The service can run locally with Uvicorn or be packaged using Docker. An AWS App Runner deployment flow is documented in `AWS_DEPLOYMENT.md`.

## Project Architecture

```text
debug_knowledge.md  ->  Markdown knowledge base for RTL/EDA debug issues
rag.py              ->  Retrieves matching debug context
mcp_server.py       ->  Provides MCP tools for log parsing and context retrieval
agent.py            ->  Generates Markdown debug reports
app.py              ->  FastAPI cloud-ready API wrapper
Dockerfile          ->  Container configuration
AWS_DEPLOYMENT.md   ->  AWS App Runner deployment documentation
```

## API Routes

```text
GET /
POST /debug
```

## Example Debug Request

```json
{
  "log_text": "Warning: Width mismatch in assignment at alu.v line 24\nError: Port data_in expects 8 bits but connected signal has 4 bits"
}
```

## Example Output

```json
{
  "issue_type": "WIDTH_MISMATCH",
  "errors": [
    "Error: Port data_in expects 8 bits but connected signal has 4 bits"
  ],
  "warnings": [
    "Warning: Width mismatch in assignment at alu.v line 24"
  ],
  "retrieved_context": "WIDTH_MISMATCH...",
  "markdown_report": "# EDA Debug Report..."
}
```

## Skills Demonstrated

This project demonstrates Python scripting, FastAPI development, AI-assisted debug workflows, RAG-style context retrieval, MCP tool integration, FPGA and RTL log analysis, technical documentation, knowledge base content, Docker configuration, and AWS deployment planning.