# Notebook validation

**Execution date:** 28 September 2026  
**Result:** local audit: 28 / 28 notebooks and 332 / 332 code cells completed; subsequent GitHub Actions Jupyter-kernel execution: 28 / 28 notebooks passed.

## Local audit method

Each notebook ran in a separate fresh Python process with an initially empty working directory. An IPython `InteractiveShell` executed every code cell from top to bottom, with the Matplotlib inline backend enabled. Standard output, rich output, figures, and exceptions were captured. The executable source cells were unchanged.

This checks that the notebook's own setup and core exercises run in the recorded environment. It also exercises the standalone bootstrap paths in Chapters 2 and 28, where support files are created when absent.

## Recorded local audit environment

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

## Local audit chapter results

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

## Confirmed GitHub Actions execution

[Notebook smoke test — run 36489488328](https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks/actions/runs/36489488328) completed with **success** on 28 September 2026 at 22:01 UTC. The run used branch `main`, commit [`b84ef3c428d2e19bcfde3996d7c3a7871276db21`](https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks/commit/b84ef3c428d2e19bcfde3996d7c3a7871276db21). The `execute-notebooks` job and its `Execute notebooks` step both passed.

The [workflow](../.github/workflows/notebook-smoke-test.yml) selected Python 3.12 on `ubuntu-latest`, installed `requirements.txt`, and ran [`scripts/validate_notebooks.py`](../scripts/validate_notebooks.py). That script requires exactly 28 notebooks, validates their notebook structure, and executes each with `nbclient` using a separate `python3` Jupyter kernel and a fresh temporary working directory. Execution stops on an error; each code cell has a 600-second timeout.

This CI result adds actual Jupyter-kernel execution to the local IPython-process audit above. The exact versions in the preceding environment table describe the local audit; they are not a separately captured full CI environment. The workflow requests the same scientific package pins. Neither check is a hosted Colab or browser-interface test, and neither establishes physical-device behavior. [Machine-readable CI summary](github-actions-validation.json).

## Scope and limits

- The local audit environment did not permit TCP or IPC socket binding. That audit used isolated IPython processes; the subsequent successful CI run used real Jupyter kernels. Neither check drove the JupyterLab browser interface.
- Hosted Google Colab execution and its authentication/sharing interface were not tested by either check.
- Passing execution confirms the absence of runtime exceptions under these conditions; it does not independently prove every scientific claim, external source, or hardware behavior.
- Timing values depend on the machine and runtime. Floating-point results and plots may vary with software versions.
- Chapter 19 subsequently received four missing exercise headings in Markdown. Chapter 21 received a comment and takeaway terminology correction, then passed an additional 11-cell rerun with unchanged standard output. Numerical behavior was unchanged.

To reproduce the learning workflow, install the declared environment, open one notebook in JupyterLab, restart its kernel, and run every cell from the beginning. Use a clean working copy when reproducing a baseline because some notebooks preserve editable files created by an earlier run.
