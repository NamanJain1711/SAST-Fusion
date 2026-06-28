import subprocess
from colorama import Fore, Style

ERROR_MAP = {

    "returned non-zero exit status":
        "The selected module could not complete successfully.",

    "No such file":
        "The specified file or folder could not be found.",

    "Permission denied":
        "The output file is currently open. Please close it and try again.",

    "No module named":
        "A required Python package is missing. Please install the project dependencies.",

    "JSONDecodeError":
        "The configuration file contains invalid JSON.",

    "WinError 2":
        "A required executable or file could not be located."
}


def handle_exception(e):

    message = str(e)

    for key, value in ERROR_MAP.items():

        if key.lower() in message.lower():
            message = value
            break

    print()
    print(Fore.RED + "=" * 60)
    print(Fore.RED + Style.BRIGHT + "ERROR".center(60))
    print(Fore.RED + "=" * 60)
    print()

    print(Fore.YELLOW + message)
    print()
    print(Fore.CYAN + "Please review your inputs and try again.")
    print()
    print(Fore.RED + "=" * 60)