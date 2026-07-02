# SAST Fusion v1.1

Static Application Security Automation Toolkit

---

## Overview

SAST Fusion is a Python-based Application Security Automation Toolkit designed to automate common Secure Code Review activities.

The toolkit consolidates multiple security assessment modules into a single command-line interface.

Current capabilities include:

- Fortify Findings Parser
- Custom Regex Scanner
- Advanced Rules Engine
- Semgrep Integration
- Technology Discovery
- Software Composition Analysis (SCA)
- Report Consolidator

---

## Features

### Fortify Findings Parser

- Parse Fortify FPR files
- Export findings to Excel
- Group duplicate vulnerabilities
- Severity based sorting

---

### Custom Rules Engine

- Regex based source code scanning
- Configurable JSON rules
- Excel reporting
- Severity classification

---

### Advanced Rules Engine

- Improved regex detection
- Confidence based findings
- Enhanced reporting

---

### Semgrep Integration

- Execute Semgrep scans
- Parse results
- Export findings

---

### Technology Discovery

Automatically detects

- Programming Languages
- Frameworks
- Package Managers
- Databases
- Configuration Files

---

### Software Composition Analysis

Powered by Trivy

Features

- Dependency Scanning
- CVE Detection
- Severity Classification
- Fixed Version Detection
- Duplicate Consolidation
- Excel Reporting

---

### Report Consolidator

Merge multiple reports into one.

Supports

- Excel
- CSV

Automatically removes duplicate findings.

---

## Project Structure

```
SAST_Fusion/

│
├── toolkit.py
│
├── modules/
│   ├── fortify_parser.py
│   ├── scanner_v1.py
│   ├── scanner_v2.py
│   ├── semgrep_scanner.py
│   ├── technology_analyzer.py
│   ├── sca_scanner.py
│   ├── trivy_parser.py
│   ├── sca_excel.py
│   ├── merge_excel.py
│   ├── console.py
│   └── error_handler.py
│
├── rules/
│
├── output/
│
├── temp/
│
├── requirements.txt
│
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/NamanJain1711/SAST-Fusion/
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Trivy

https://trivy.dev/latest/getting-started/installation/

Ensure Trivy is available in your PATH.

---

## Usage

Run

```bash
python toolkit.py
```

---

## Available Modules

```
1. Fortify Findings Parser

2. Custom Rules Engine

3. Advanced Rules Engine

4. Semgrep Integration

5. Technology Discovery

6. Software Composition Analysis (SCA)

7. Report Consolidator

8. Exit
```

---

## Outputs

All generated reports are saved inside

```
output/
```

Example

```
Fortify_Findings.xlsx

Custom_Rules_Engine.xlsx

Advanced_Rules_Engine.xlsx

Semgrep_Findings.xlsx

Technology_Discovery.xlsx

SCA_Findings.xlsx

Report_Consolidator.xlsx
```

---

## Requirements

Python 3.11+

Trivy

Semgrep

---

## Supported Platforms

Windows

Linux

---

## Version

Current Version

```
v1.1
```

---

## Roadmap

### v1.2

- Improved CLI
- Better Logging
- Additional SAST Rules

### v2.0

- AI Report Generator
- Word Report Automation
- Executive Dashboard
- AI Generated Descriptions
- AI Generated Recommendations
- Password Protected PDF Reports

---

## License

Internal Use / Proprietary
