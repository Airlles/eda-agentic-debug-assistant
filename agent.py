import os
from mcp_server import parse_eda_log, retrieve_debug_context


def analyze_log(log_text):
    parsed_result = parse_eda_log(log_text)

    issue_type = parsed_result["issue_type"]

    retrieved_context = retrieve_debug_context(issue_type)

    return parsed_result, retrieved_context

def generate_debug_report(parsed_result, retrieved_context):
    issue_type = parsed_result["issue_type"]
    errors = parsed_result["errors"]
    warnings = parsed_result["warnings"]

    report = f"""
# EDA Debug Report

## Likely Issue Type
{issue_type}

## Evidence From Log

### Errors
{errors}

### Warnings
{warnings}

## Retrieved Debug Context
{retrieved_context}

## Suggested Next Steps
1. Inspect the error and warning lines shown above.
2. Open the RTL file mentioned in the log.
3. Compare the signal declarations and module port connections.
4. Fix one issue at a time, then rerun synthesis or simulation.
"""

    return report

if __name__ == "__main__":
    available_files = []

    for file_name in os.listdir("sample_logs"):
        if file_name.endswith(".txt"):
            available_files.append(file_name)

    print("Available log files:")
    for file_name in available_files:
        print(file_name)

    print()
    selected_file = input("Enter a log file name: ")

    input_path = os.path.join("sample_logs", selected_file)

    with open(input_path, "r") as file:
        sample_log = file.read()

    parsed_result, retrieved_context = analyze_log(sample_log)

    report = generate_debug_report(parsed_result, retrieved_context)

    report_file_name = selected_file.replace(".txt", "_report.md")
    output_path = os.path.join("outputs", report_file_name)

    with open(output_path, "w") as file:
        file.write(report)

    print()
    print(report)
    print(f"Report saved to {output_path}")