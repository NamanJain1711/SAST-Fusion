#!/usr/bin/env python3

from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)


# ==========================================
# Banner
# ==========================================

def banner(title, subtitle=None):

    print()

    print(Fore.CYAN + "=" * 60)

    print(
        Fore.CYAN +
        Style.BRIGHT +
        f"{title:^60}"
    )

    if subtitle:

        print(
            Fore.WHITE +
            f"{subtitle:^60}"
        )

    print(Fore.CYAN + "=" * 60)


# ==========================================
# Information
# ==========================================

def info(message):
    print(Fore.CYAN + "[*] " + message)


# ==========================================
# Success
# ==========================================

def success(message):

    print(
        Fore.GREEN +
        Style.BRIGHT +
        "[+] " +
        message +
        Style.RESET_ALL
    )


# ==========================================
# Warning
# ==========================================

def warning(message):
    print(Fore.YELLOW + Style.BRIGHT + "[!] " + message)


# ==========================================
# Error
# ==========================================

def error(message):
    print(Fore.RED + Style.BRIGHT + "[X] " + message)


# ==========================================
# Progress
# ==========================================

def step(number, total, message):
    print(Fore.MAGENTA + f"[{number}/{total}] " + message)


# ==========================================
# Section
# ==========================================

def section(title):

    print()

    print(
        Fore.BLUE +
        "-" * 60
    )

    print(
        Fore.BLUE +
        Style.BRIGHT +
        title
    )

    print(
        Fore.BLUE +
        "-" * 60
    )


# ==========================================
# Completed
# ==========================================

def completed():

    print(
        Fore.GREEN +
        "✔ Completed"
    )


# ==========================================
# Failed
# ==========================================

def failed():

    print(
        Fore.RED +
        "✖ Failed"
    )


# ==========================================
# Output File
# ==========================================

def output(path):

    print()

    print(
        Fore.GREEN +
        Style.BRIGHT +
        "Output"
    )

    print(
        Fore.WHITE +
        path
    )


# ==========================================
# Footer
# ==========================================

def footer():

    print()

    print(
        Fore.CYAN +
        "=" * 60
    )

# ==========================================
# Menu Option
# ==========================================

def menu_option(number, text):

    print(
        Fore.YELLOW +
        f"{number}. " +
        Fore.WHITE +
        text
    )

# ==========================================
# Prompt
# ==========================================

def prompt(message):

    return input(
        Fore.GREEN +
        message +
        Style.RESET_ALL
    )

# ==========================================
# Title
# ==========================================

def title(text):

    print()

    print(
        Fore.BLUE +
        Style.BRIGHT +
        text
    )

    print(
        Fore.BLUE +
        "-" * len(text)
    )

# ==========================================
# Separator
# ==========================================

def separator():

    print(
        Fore.CYAN +
        "=" * 60
    )

# ==========================================
# Status
# ==========================================

def status(module, state):

    color = Fore.GREEN

    if state.lower() == "failed":
        color = Fore.RED

    elif state.lower() == "warning":
        color = Fore.YELLOW

    print()

    print(Fore.CYAN + "=" * 60)

    print(
        Fore.WHITE +
        "Module : " +
        Fore.CYAN +
        module
    )

    print(
        Fore.WHITE +
        "Status : " +
        color +
        state
    )

    print(Fore.CYAN + "=" * 60)

# ==========================================
# Header
# ==========================================

def header(title):

    print()

    print(
        Fore.BLUE +
        "=" * 60
    )

    print(
        Fore.BLUE +
        Style.BRIGHT +
        f"{title:^60}"
    )

    print(
        Fore.BLUE +
        "=" * 60
    )

# ==========================================
# Goodbye
# ==========================================

def goodbye():

    print()

    print(
        Fore.GREEN +
        Style.BRIGHT +
        "Thank you for using SAST Fusion."
    )

    print()