# Agentic AI Debug Assistant for RTL and EDA Log Analysis

## Overview

The Agentic AI Debug Assistant is a prototype tool for analyzing RTL and EDA log files. It reads Quartus or ModelSim style logs, identifies common hardware development issues, retrieves relevant debugging guidance from a local knowledge base, and generates structured markdown reports.

The project combines Python parsing, retrieval augmented generation, MCP exposed tools, and an agentic workflow in a hardware debugging context.

## What It Does

The assistant takes an EDA log file as input and produces a debug report that includes:

1. The likely issue type
2. Error lines found in the log
3. Warning lines found in the log
4. Retrieved debugging context
5. Suggested next inspection steps

The current prototype supports common RTL and EDA issues such as width mismatches, missing modules, timing violations, unconnected nets, and syntax errors.

## Tools Used

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Visual Studio Code | Development environment |
| MCP | Exposes parser and retrieval functions as callable tools |
| Markdown | Knowledge base and generated reports |
| Terminal | Runs the assistant and generates reports |

## Python Libraries Used

| Library | Purpose |
|---|---|
| `mcp` | Defines MCP tools for parsing and retrieval |
| `os` | Lists files and builds file paths |
| `pprint` | Formats test output during development |

## Key Concepts

### Retrieval Augmented Generation

The project uses a local markdown file as a small knowledge base. When an issue type is detected, the assistant retrieves the matching section from the knowledge base and includes that information in the final report.

### Model Context Protocol

The project uses MCP to expose Python functions as tools. These tools handle log parsing and debug context retrieval.

### Agentic Workflow

The assistant follows a tool based workflow instead of simply summarizing text. It reads the selected log, calls the parser, retrieves relevant context, generates a report, and saves the result.

## Project Structure

```text
eda_agentic_debug_assistant/
├── agent.py
├── mcp_server.py
├── rag.py
├── debug_knowledge.md
├── requirements.txt
├── sample_logs/
│   ├── width_mismatch.txt
│   ├── missing_module.txt
│   ├── timing_violation.txt
│   └── unconnected_net.txt
└── outputs/
    ├── width_mismatch_report.md
    ├── missing_module_report.md
    ├── timing_violation_report.md
    └── unconnected_net_report.md
```

## File Overview

| File | Description |
|---|---|
| `agent.py` | Main workflow controller that reads logs, calls tools, and saves reports |
| `mcp_server.py` | Defines MCP exposed tools for parsing and retrieval |
| `rag.py` | Retrieves matching debug guidance from the knowledge base |
| `debug_knowledge.md` | Local knowledge base for common RTL and EDA issues |
| `sample_logs/` | Contains example input logs |
| `outputs/` | Stores generated debug reports |
| `requirements.txt` | Lists required Python packages |

## Supported Issue Types

```text
WIDTH_MISMATCH
MISSING_MODULE
TIMING_VIOLATION
UNCONNECTED_NET
SYNTAX_ERROR
UNKNOWN
```

## Installation

Install the required package:

```bash
pip install --user mcp
```

If needed, use:

```bash
py -m pip install --user mcp
```

## How to Run

Open a terminal in the project folder:

```bash
cd d:\eda_agentic_debug_assistant
```

Run the assistant:

```bash
python agent.py
```

The program will show the available log files:

```text
Available log files:
missing_module.txt
timing_violation.txt
unconnected_net.txt
width_mismatch.txt
```

Enter one file name when prompted:

```text
width_mismatch.txt
```

The assistant will analyze the selected log and save a report in the `outputs` folder.

## Demo

Example input:

```text
Warning: Width mismatch in assignment at alu.v line 24
Warning: Signal result expects 8 bits but expression provides 4 bits
Error: Port data_in of module alu_core expects 8 bits but connected signal sw_input has 4 bits
```

Example generated report:

```md
# EDA Debug Report

## Likely Issue Type
WIDTH_MISMATCH

## Evidence From Log

### Errors
Error: Port data_in of module alu_core expects 8 bits but connected signal sw_input has 4 bits

### Warnings
Warning: Width mismatch in assignment at alu.v line 24
Warning: Signal result expects 8 bits but expression provides 4 bits

## Retrieved Debug Context
A width mismatch happens when two signals with different bit widths are connected or assigned.

## Suggested Next Steps
1. Inspect the error and warning lines shown above.
2. Open the RTL file mentioned in the log.
3. Compare the signal declarations and module port connections.
4. Fix one issue at a time, then rerun synthesis or simulation.
```

## Example Workflow

```text
User selects a log file
→ agent reads the log
→ MCP parser tool classifies the issue
→ RAG retrieval finds matching debug context
→ agent generates a markdown report
→ report is saved to outputs
```

## Future Improvements

1. Add real Quartus, ModelSim, and Vivado log examples.
2. Add automatic file name and line number extraction.
3. Add support for multiple issue types in one log.
4. Add a Verilog parser for signal declarations and module ports.
5. Add confidence scoring for issue classification.
6. Add a Streamlit interface for uploading logs.
7. Add unit tests for each issue type.
8. Add GitHub Actions for automated parser testing.
9. Add vector retrieval using Chroma or FAISS.

## Author

Hani Ahmed