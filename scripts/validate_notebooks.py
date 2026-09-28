"""Execute each self-contained chapter notebook with its own kernel and directory."""
from pathlib import Path
import tempfile
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]

def main():
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    if len(notebooks) != 28:
        raise RuntimeError(f"Expected 28 chapter notebooks, found {len(notebooks)}")
    for path in notebooks:
        print(f"Executing {path.name}", flush=True)
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        with tempfile.TemporaryDirectory(prefix=path.stem + "-") as work:
            NotebookClient(
                notebook, timeout=600, kernel_name="python3", allow_errors=False,
                resources={"metadata": {"path": work}},
            ).execute()
    print(f"PASS: {len(notebooks)} notebooks executed without errors.")

if __name__ == "__main__":
    main()
