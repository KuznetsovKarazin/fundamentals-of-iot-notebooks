"""Remove outputs and execution counts from Jupyter notebooks.

Usage:
    python scripts/clean_notebooks.py
"""

from __future__ import annotations

import json
from pathlib import Path


def clean_notebook(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    for path in sorted(Path("notebooks").glob("*.ipynb")):
        clean_notebook(path)
        print(f"Cleaned {path}")


if __name__ == "__main__":
    main()
