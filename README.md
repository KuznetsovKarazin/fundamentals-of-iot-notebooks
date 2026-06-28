# Fundamentals of the Internet of Things — Practical Notebooks

This repository contains practical Jupyter/Google Colab notebooks accompanying the textbook:

**Oleksandr Kuznetsov, _Fundamentals of the Internet of Things_**

The repository is intended as a transparent and reproducible companion resource for students, instructors, and readers of the textbook. Google Drive copies may be used as a mirror, but this GitHub repository should be treated as the stable public source after release.

## Current contents

| Chapter | Topic | Notebook | Open in Colab |
|---|---|---|---|
| Ch. 10 | Common IoT Sensors | [`ch10-common-iot-sensors-practice.ipynb`](https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch10-common-iot-sensors-practice.ipynb) | [Open in Colab](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch10-common-iot-sensors-practice.ipynb) |

## Chapter 10 notebook

The first notebook includes hands-on Python exercises for Chapter 10, **Common IoT Sensors**:

1. Temperature sensor network with data fusion.
2. Environmental monitoring with temperature and pressure filtering.
3. MEMS IMU simulation with accelerometer–gyroscope complementary filtering.
4. Humidity sensor comparison: capacitive vs. resistive sensors.

The notebook uses only standard scientific Python packages: `numpy`, `matplotlib`, and `scipy`.

## Recommended use

In Google Colab:

1. Open the notebook using the Colab link in the table above.
2. Select **Runtime → Run all**.
3. Work through the challenge tasks at the end of each exercise.
4. Save your own copy if you want to modify the notebook.

For local execution:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate      # Windows PowerShell

pip install -r requirements.txt
jupyter notebook
```

## Repository structure

```text
notebooks/   Jupyter notebooks organized by textbook chapter
data/        Small public sample datasets, if needed
assets/      Figures and auxiliary materials
docs/        Indexes and repository documentation
scripts/     Utility scripts for notebook maintenance
```

## Naming convention

Use stable, lowercase file names:

```text
ch10-common-iot-sensors-practice.ipynb
ch11-advanced-sensor-technologies-practice.ipynb
ch12-actuators-and-control-practice.ipynb
```

Avoid renaming notebooks after links or QR codes have been included in the book.

## Citation

If you use these materials in teaching or research, please cite the textbook and this repository. A `CITATION.cff` file is included so GitHub can generate citation metadata.

## License

Code cells and small utility scripts are released under the MIT License, unless stated otherwise.

Educational text, exercise statements, figures, and explanatory content are released under the Creative Commons Attribution-NonCommercial 4.0 International license, unless stated otherwise.

The textbook itself is not included in this repository.
