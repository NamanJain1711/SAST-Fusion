#!/usr/bin/env python3

import json
from collections import defaultdict


def parse_trivy_json(json_file):

    with open(
        json_file,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    findings = defaultdict(
        lambda: {
            "package": "",
            "version": "",
            "cve": "",
            "severity": "",
            "fixed_version": "",
            "scanner": "Trivy",
            "dependency_files": set()
        }
    )

    for result in data.get("Results", []):

        dependency = result.get(
            "Target",
            "Unknown"
        )

        vulnerabilities = result.get(
            "Vulnerabilities",
            []
        )

        for vuln in vulnerabilities:

            package = vuln.get(
                "PkgName",
                ""
            )

            version = vuln.get(
                "InstalledVersion",
                ""
            )

            cve = vuln.get(
                "VulnerabilityID",
                ""
            )

            severity = vuln.get(
                "Severity",
                ""
            ).title()

            fixed = vuln.get(
                "FixedVersion",
                ""
            )

            key = (
                package,
                version,
                cve
            )

            findings[key]["package"] = package
            findings[key]["version"] = version
            findings[key]["cve"] = cve
            findings[key]["severity"] = severity
            findings[key]["fixed_version"] = fixed

            findings[key]["dependency_files"].add(
                dependency
            )

    normalized = []

    for finding in findings.values():

        normalized.append(

            {
                "package":
                    finding["package"],

                "version":
                    finding["version"],

                "cve":
                    finding["cve"],

                "severity":
                    finding["severity"],

                "fixed_version":
                    finding["fixed_version"],

                "scanner":
                    finding["scanner"],

                "occurrences":
                    len(
                        finding["dependency_files"]
                    ),

                "dependency_files":
                    sorted(
                        list(
                            finding["dependency_files"]
                        )
                    )
            }

        )

    return normalized