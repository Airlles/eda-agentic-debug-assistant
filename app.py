from fastapi import FastAPI
from pydantic import BaseModel
from agent import analyze_log, generate_debug_report


app = FastAPI(
    title="Cloud-Deployed AI Debug Assistant for FPGA and RTL Logs",
    description="Cloud-ready API for parsing FPGA/RTL logs, retrieving debug context, and generating Markdown reports.",
    version="1.0.0"
)


class LogRequest(BaseModel):
    log_text: str


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI RTL Debug Assistant",
        "cloud_ready": True
    }


@app.post("/debug")
def debug_log(request: LogRequest):
    parsed_result, retrieved_context = analyze_log(request.log_text)
    markdown_report = generate_debug_report(parsed_result, retrieved_context)

    return {
        "issue_type": parsed_result["issue_type"],
        "errors": parsed_result["errors"],
        "warnings": parsed_result["warnings"],
        "retrieved_context": retrieved_context,
        "markdown_report": markdown_report
    }