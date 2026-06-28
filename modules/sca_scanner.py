#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

from trivy_parser import parse_trivy_json
from sca_excel import create_sca_excel
from console import *

Path("output").mkdir(exist_ok=True)
Path("temp").mkdir(exist_ok=True)

JSON_OUTPUT = "temp\\SCA_results.json"


def run_trivy(source_folder):

    print("\nRunning SCA Scan...\n")

    cmd = [

        "trivy",
        "fs",
        source_folder,
        "--format",
        "json",
        "-o",
        JSON_OUTPUT

    ]

    subprocess.run(cmd, check=True)

    success("Scan Completed.")


def main():

    if len(sys.argv) != 2:

        print(
            "Usage: python sca_scanner.py <source_folder>"
        )

        sys.exit(1)

    source_folder = sys.argv[1]

    if not Path(source_folder).exists():

        failed("Source folder not found.")

        sys.exit(1)

    run_trivy(source_folder)

    findings = parse_trivy_json(JSON_OUTPUT)

    create_sca_excel(findings)

    success("\nSCA_Findings.xlsx generated successfully.")


def run():
    main()


from error_handler import handle_exception

if __name__ == "__main__":

    try:

        main()

    except Exception as e:

        handle_exception(e)