import subprocess
import sys
import shlex
from modules.console import *
from modules.error_handler import handle_exception

import os

os.system("cls" if os.name == "nt" else "clear")

def run_module(args):

    try:

        subprocess.run(
            args,
            check=True,
            capture_output=False
        )

    except subprocess.CalledProcessError as e:

        handle_exception(e)

    except Exception as e:

        handle_exception(e)

    finally:

        input("\nPress Enter to continue...")

def validate_path(path, name="Source Folder"):

    if not path:

        warning(f"{name} was not provided.")
        return False

    if not os.path.exists(path):

        warning(f"{name} does not exist.")
        return False

    return True

while True:

    try:

        banner(
            "SAST Fusion v1.1",
            "Static Application Security Automation Toolkit"
        )

        menu_option(1, "Fortify Findings Parser")
        menu_option(2, "Custom Rules Engine")
        menu_option(3, "Advanced Rules Engine")
        menu_option(4, "Semgrep Integration")
        menu_option(5, "Technology Discovery")
        menu_option(6, "Software Composition Analysis (SCA)")
        menu_option(7, "Report Consolidator")
        menu_option(8, "Exit")

        
        choice = prompt("\nSelect Option: ")

        if choice == "1":

            fprs = shlex.split(
                prompt("\nEnter FPR file(s): ").strip()
            )

            if not fprs:
                warning("No FPR file selected.")
                continue

            run_module([
                sys.executable,
                "modules\\fortify_parser.py",
                *fprs
            ])
            

        elif choice == "2":

            path = prompt("\nSource Folder: ").strip().strip('"')

            if not path:

                warning("No source folder selected.")
                continue

            if not os.path.exists(path):

                warning("The specified path does not exist.")
                continue

            run_module([
                sys.executable,
                "modules\\scanner_v1.py",
                path
            ])

        elif choice == "3":

            path = prompt("\nSource Folder: ").strip().strip('"')

            if not path:

                warning("No source folder selected.")
                continue

            if not os.path.exists(path):

                warning("The specified path does not exist.")
                continue

            run_module([
                sys.executable,
                "modules\\scanner_v2.py",
                path
            ])

        elif choice == "4":

            path = prompt("\nSource Folder: ").strip().strip('"')

            if not path:

                warning("No source folder selected.")
                continue

            if not os.path.exists(path):

                warning("The specified path does not exist.")
                continue

            run_module([
                sys.executable,
                "modules\\semgrep_scanner.py",
                path
            ])

        elif choice == "5":

            path = prompt("\nSource Folder: ").strip().strip('"')

            if not path:

                warning("No source folder selected.")
                continue

            if not os.path.exists(path):

                warning("The specified path does not exist.")
                continue

            run_module([
                sys.executable,
                "modules\\technology_analyzer.py",
                path
            ])

           
        elif choice == "6":

            path = prompt("\nSource Folder: ").strip().strip('"')

            if not path:

                warning("No source folder selected.")
                continue

            if not os.path.exists(path):

                warning("The specified path does not exist.")
                continue

            run_module([
                sys.executable,
                "modules\\sca_scanner.py",
                path
            ])

            
        elif choice == "7":


            file1 = prompt("\nFirst Excel: ").strip().strip('"')
            file2 = prompt("\nSecond Excel: ").strip().strip('"')
            output = prompt("\nOutput File: ").strip().strip('"')

            if not os.path.exists(file1):

                warning("First report not found.")
                continue

            if not os.path.exists(file2):

                warning("Second report not found.")
                continue


            run_module([
                sys.executable,
                "modules\\merge_excel.py",
                file1,
                file2,
                output
            ])

        elif choice == "8":

            goodbye()
            break

        else:

            warning("Invalid option selected.")

    except Exception as e:

        handle_exception(e)