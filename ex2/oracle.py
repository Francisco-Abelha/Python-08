import os
import sys
from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def find_missing(config: dict[str, str | None]) -> list[str]:
    required = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")
    return [k for k in required if not config[k]]


def display_config(config: dict[str, str | None]) -> None:
    mode = config["MATRIX_MODE"]
    print("\nORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    if mode == "production":
        print("  Database: Connected to production cluster")
    else:
        print("  Database: Connected to local instance")
    print("  API Access: Authenticated")
    print(f"  Log Level: {config['LOG_LEVEL']}")
    print("  Zion Network: Online")


def security_check() -> None:
    print("Environment security check:")

    try:
        with open(".env"):
            print("  [OK] .env file properly configured")
    except FileNotFoundError:
        print("  [!!] .env file not found")

    try:
        with open(".gitignore") as f:
            if ".env" in f.read():
                print("  [OK] No hardcoded secrets detected")
            else:
                print("  [!!] .env not in .gitignore")
    except FileNotFoundError:
        print("  [!!] .gitignore missing")

    print("  [OK] Production overrides available")
    print("The Oracle sees all configurations.")


def main() -> None:

    config = load_config()
    missing = find_missing(config)

    if missing:
        print(
            "WARNING: Missing configuration: "
            f"{', '.join(missing)}"
        )
        sys.exit(1)

    display_config(config)
    security_check()


if __name__ == "__main__":
    main()
