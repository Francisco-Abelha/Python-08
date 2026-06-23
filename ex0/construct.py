import os
import sys
import site


def main() -> None:

    if sys.exec_prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print(
            "Virtual Environment: None detected\n"
            "\nWARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
            "\nTo enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
        )

    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"Environment Path: {sys.exec_prefix}\n")
        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n\n"
            "Package installation path:\n"
        )
        print(site.USER_SITE)


if __name__ == "__main__":
    main()
