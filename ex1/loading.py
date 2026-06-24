import importlib


def compare_package_managers(installed: list[tuple[str, str]]) -> None:
    print("\nPACKAGE MANAGER COMPARISON:\n")

    print("Installed packages:")
    for name, version in installed:
        print(f"    {name:<12} {version}")

    print("\n            pip                       Poetry")
    print("Manifest    requirements.txt          pyproject.toml")
    print("Pinning     manual (==)               constraints (^) + resolver")
    print("Lockfile    none                      poetry.lock (reproducible)")
    print("Resolver    none, installs in order   resolves conflicts upfront")
    print("Env mgmt    venv + pip (separate)     built-in (poetry install)")

    print("\nConfig files detected:")
    for filename in ("requirements.txt", "pyproject.toml", "poetry.lock"):
        try:
            with open(filename):
                status = "yes"
        except FileNotFoundError:
            status = "no"
        print(f"    {filename:<18}: {status}")

    print(
        "\nExample: Poetry's resolver blocked install when matplotlib 3.11\n"
        "required Python >=3.11 but the project allowed >=3.10, catching the\n"
        "conflict before installing. pip does not check this in advance."
    )


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    packages = [
        ("numpy", "Numerical computation ready"),
        ("pandas", "Data manipulation ready"),
        ("matplotlib", "Visualization ready"),
    ]

    missing = []
    installed = []
    for name, description in packages:
        try:
            module = importlib.import_module(name)
            version = module.__version__
            print(f"[OK] {name} {version} - {description}")
            installed.append((name, version))
        except ModuleNotFoundError:
            missing.append(name)

    if missing:
        print(f"WARNING: Missing dependencies: {', '.join(missing)}\n")
        print("To load these programs, install the required packages.\n")
        print(
            "Using pip:\n"
            "    pip install -r requirements.txt\n\n"
            "Using Poetry:\n"
            "    poetry install\n"
            "    poetry run python loading.py\n\n"
            "Then run this program again."
        )
        return
    else:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        compare_package_managers(installed)

        print("\nAnalyzing Matrix data...")
        rng = np.random.default_rng(42)
        print("Processing 1000 data points...")
        numpy_array = rng.random((100, 10))
        col_names = [
            "Sig_1",
            "Sig_2",
            "Sig_3",
            "Sig_4",
            "Sig_5",
            "Sig_6",
            "Sig_7",
            "Sig_8",
            "Sig_9",
            "Sig_10"
        ]

        df = pd.DataFrame(numpy_array, columns=col_names)
        plot_data = df.cumsum()
        plt.plot(plot_data)
        print("Generating visualization...\n")
        plt.savefig("matrix_analysis.png")
        plt.close()
        print(
            "Analysis complete!\n",
            "Results saved to: matrix_analysis.png"
        )


if __name__ == "__main__":
    main()
