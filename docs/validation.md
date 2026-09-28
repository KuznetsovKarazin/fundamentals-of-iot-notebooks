# Notebook validation

**Execution date:** 28 September 2026  
**Result:** 28 / 28 notebooks completed; 332 / 332 code cells executed without an exception.

## Method

Each notebook ran in a separate fresh Python process with an initially empty working directory. An IPython `InteractiveShell` executed every code cell from top to bottom, with the Matplotlib inline backend enabled. Standard output, rich output, figures, and exceptions were captured. The executable source cells were unchanged.

This checks that the notebook's own setup and core exercises run in the recorded environment. It also exercises the standalone bootstrap paths in Chapters 2 and 28, where support files are created when absent.

## Environment

| Component | Version |
|:--|:--|
| Python | 3.12.14 |
| Operating system | Linux x86_64 |
| numpy | 2.3.5 |
| pandas | 2.2.3 |
| matplotlib | 3.10.8 |
| scipy | 1.17.0 |
| scikit-learn | 1.8.0 |
| networkx | 3.7 |
| cbor2 | 6.1.4 |
| IPython | 9.17.1 |
| nbformat | 5.11.1 |
| matplotlib-inline | 0.2.2 |

The scientific package versions are declared in [`requirements.txt`](../requirements.txt) and [`environment.yml`](../environment.yml). JupyterLab and ipykernel are interface dependencies; their supported ranges are separate from the scientific versions above.

## Chapter results

| Chapter | Code cells executed | Result |
|:--|--:|:--|
| 01 | 5 | Passed |
| 02 | 7 | Passed |
| 03 | 12 | Passed |
| 04 | 9 | Passed |
| 05 | 12 | Passed |
| 06 | 11 | Passed |
| 07 | 9 | Passed |
| 08 | 9 | Passed |
| 09 | 12 | Passed |
| 10 | 13 | Passed |
| 11 | 23 | Passed |
| 12 | 9 | Passed |
| 13 | 12 | Passed |
| 14 | 12 | Passed |
| 15 | 13 | Passed |
| 16 | 10 | Passed |
| 17 | 13 | Passed |
| 18 | 10 | Passed |
| 19 | 12 | Passed |
| 20 | 15 | Passed |
| 21 | 11 | Passed |
| 22 | 13 | Passed |
| 23 | 15 | Passed |
| 24 | 11 | Passed |
| 25 | 19 | Passed |
| 26 | 11 | Passed |
| 27 | 14 | Passed |
| 28 | 10 | Passed |

## Scope and limits

- The execution environment did not permit TCP or IPC socket binding for a Jupyter kernel. The check therefore used isolated IPython processes, rather than a live Jupyter browser session.
- Hosted Google Colab execution and its authentication/sharing interface were not tested by this run.
- Passing execution confirms the absence of runtime exceptions under these conditions; it does not independently prove every scientific claim, external source, or hardware behavior.
- Timing values depend on the machine and runtime. Floating-point results and plots may vary with software versions.
- Chapter 19 subsequently received four missing exercise headings in Markdown. Chapter 21 received a comment and takeaway terminology correction, then passed an additional 11-cell rerun with unchanged standard output. Numerical behavior was unchanged.

To reproduce the learning workflow, install the declared environment, open one notebook in JupyterLab, restart its kernel, and run every cell from the beginning. Use a clean working copy when reproducing a baseline because some notebooks preserve editable files created by an earlier run.
