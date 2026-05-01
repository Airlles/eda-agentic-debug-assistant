from mcp.server.fastmcp import FastMCP
from rag import retrieve_context
from pprint import pprint

mcp = FastMCP("eda_debug_tools")


@mcp.tool()
def parse_eda_log(log_text: str) -> dict:
    lower_log = log_text.lower()

    issue_type = "UNKNOWN"

    if "width mismatch" in lower_log or "expects 8 bits" in lower_log:
        issue_type = "WIDTH_MISMATCH"

    elif "module not found" in lower_log or "can't find module" in lower_log:
        issue_type = "MISSING_MODULE"

    elif "timing violation" in lower_log or "slack" in lower_log:
        issue_type = "TIMING_VIOLATION"

    elif "unconnected" in lower_log or "undriven" in lower_log:
        issue_type = "UNCONNECTED_NET"

    elif "syntax error" in lower_log or "near text" in lower_log:
        issue_type = "SYNTAX_ERROR"

    errors = []
    warnings = []

    for line in log_text.splitlines():
        if "error" in line.lower():
            errors.append(line.strip())

        elif "warning" in line.lower():
            warnings.append(line.strip())

    return {
        "issue_type": issue_type,
        "errors": errors,
        "warnings": warnings
    }


@mcp.tool()
def retrieve_debug_context(issue_type: str) -> str:
    context = retrieve_context(issue_type)

    return context


if __name__ == "__main__":
    sample_log = """
    Warning: Width mismatch in assignment at alu.v line 24
    Error: Port data_in expects 8 bits but connected signal has 4 bits
    """

    parsed_result = parse_eda_log(sample_log)
    pprint(parsed_result)

    print()
    context = retrieve_debug_context(parsed_result["issue_type"])
    print(context[:500])