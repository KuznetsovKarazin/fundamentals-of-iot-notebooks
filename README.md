# Fundamentals of the Internet of Things

### Practical notebooks for students, instructors, and independent learners

**Oleksandr Kuznetsov · eCampus University, Italy**

The Python companion to *Fundamentals of the Internet of Things*, a textbook in preparation for Morgan Kaufmann / Elsevier. Explore IoT engineering through **28 chapter notebooks**: start with virtual telemetry, investigate sensors and communication systems, then plan a reproducible deployment or capstone project.

The learning loop is simple: **run → inspect → modify → rerun → explain**. The core exercises use a CPU runtime and do not require a physical IoT board. Read the assumptions in each notebook: simulated signals and illustrative planning data are not measurements from a real deployment.

[Start with Chapter 1](notebooks/ch01-first-steps-python-colab.ipynb) · [Notebook index](docs/notebook-index.md) · [Package contents](PACKAGE_CONTENTS.md)

## Start in Google Colab

1. Choose **Run** for a chapter in the table below to open the versioned notebook in Colab.
2. Save a copy to your own Drive before editing. Use a standard Python CPU runtime.
3. Read the setup cells, then choose **Runtime → Run all**. Run from the top in a fresh runtime when checking reproducibility.
4. Inspect the tables and plots, try the challenge tasks, and explain how your changed assumptions affect the result.

GitHub-backed Colab links require repository access while this repository is private. You can also [download the checked 28-notebook snapshot from Google Drive](https://drive.google.com/file/d/1I9LOAvg60-IoF98NInUrroKNQ8DnRJaX/view), extract it, and select **File → Upload notebook** in Colab. This dated ZIP is the current Drive snapshot; individual chapter copies are still awaiting synchronization. Record the GitHub commit or the dated snapshot when reporting which version you ran.

## Choose a learning track

These tracks follow the book's table of contents. The suggested durations assume teaching time for theory, discussion, and exercises.

| Track | Chapters | Suggested duration | Focus |
|:--|:--|:--|:--|
| Short introductory course | 1–9, 22, 25 | 10–12 weeks | Foundations, platforms, sensing, MQTT, and HTTP |
| Sensors and data | 1–16 | 12–15 weeks | Sensing, acquisition, processing, integration, and calibration |
| Communications | 1–9, 17–26 | 12–15 weeks | Wireless systems, application protocols, and stack selection |
| Full IoT course | 1–26 | 20–24 weeks | Foundations through protocol engineering |
| Advanced / research | 1–28 | Adapt to project scope | Adds deployment, capstone design, and research planning |

## Explore the chapters

**Foundations:** 1–8 · **Sensors, actuators, and data:** 9–16 · **Communications:** 17–26 · **Deployment and projects:** 27–28

| Chapter | Topic | Notebook | Colab |
|:--|:--|:--:|:--:|
| 01 | Introduction to the Internet of Things | [View](notebooks/ch01-first-steps-python-colab.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch01-first-steps-python-colab.ipynb) |
| 02 | IoT and the Industry Landscape: Gaps and Opportunities | [View](notebooks/ch02-reproducible-python-project.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch02-reproducible-python-project.ipynb) |
| 03 | Defining the Internet of Things | [View](notebooks/ch03-defining-iot-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch03-defining-iot-practice.ipynb) |
| 04 | Fundamental IoT Concepts and Paradigms | [View](notebooks/ch04-fundamental-iot-concepts-paradigms-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch04-fundamental-iot-concepts-paradigms-practice.ipynb) |
| 05 | IoT Device Technologies | [View](notebooks/ch05-iot-device-technologies-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch05-iot-device-technologies-practice.ipynb) |
| 06 | IoT Gateways and Edge Processing | [View](notebooks/ch06-iot-gateways-edge-processing-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch06-iot-gateways-edge-processing-practice.ipynb) |
| 07 | IoT Platforms | [View](notebooks/ch07-iot-platforms-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch07-iot-platforms-practice.ipynb) |
| 08 | IoT Impact on Industry and Society | [View](notebooks/ch08-iot-impact-industry-society-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch08-iot-impact-industry-society-practice.ipynb) |
| 09 | Fundamentals of Sensor Technology | [View](notebooks/ch09-fundamentals-sensor-technology-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch09-fundamentals-sensor-technology-practice.ipynb) |
| 10 | Common IoT Sensors | [View](notebooks/ch10-common-iot-sensors-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch10-common-iot-sensors-practice.ipynb) |
| 11 | Advanced Sensor Technologies | [View](notebooks/ch11-advanced-sensor-technologies-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch11-advanced-sensor-technologies-practice.ipynb) |
| 12 | Actuators and Control | [View](notebooks/ch12-actuators-control-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch12-actuators-control-practice.ipynb) |
| 13 | Data Acquisition Fundamentals | [View](notebooks/ch13-data-acquisition-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch13-data-acquisition-practice.ipynb) |
| 14 | On-Board Data Processing | [View](notebooks/ch14-onboard-data-processing-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch14-onboard-data-processing-practice.ipynb) |
| 15 | Sensor and Actuator Integration | [View](notebooks/ch15-sensor-actuator-integration-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch15-sensor-actuator-integration-practice.ipynb) |
| 16 | Sensor Calibration and Maintenance | [View](notebooks/ch16-sensor-calibration-maintenance-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch16-sensor-calibration-maintenance-practice.ipynb) |
| 17 | Wireless Communication Overview | [View](notebooks/ch17-wireless-overview-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch17-wireless-overview-practice.ipynb) |
| 18 | Wi-Fi and Bluetooth for IoT | [View](notebooks/ch18-wifi-bluetooth-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch18-wifi-bluetooth-practice.ipynb) |
| 19 | Mesh Network Technologies | [View](notebooks/ch19-mesh-networks-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch19-mesh-networks-practice.ipynb) |
| 20 | Low-Power Wide-Area Networks (LPWAN) | [View](notebooks/ch20-lpwan-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch20-lpwan-practice.ipynb) |
| 21 | Cellular IoT Technologies | [View](notebooks/ch21-cellular-iot-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch21-cellular-iot-practice.ipynb) |
| 22 | MQTT Protocol | [View](notebooks/ch22-mqtt-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch22-mqtt-practice.ipynb) |
| 23 | Wired Industrial Communication Protocols | [View](notebooks/ch23-wired-industrial-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch23-wired-industrial-practice.ipynb) |
| 24 | CoAP Protocol | [View](notebooks/ch24-coap-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch24-coap-practice.ipynb) |
| 25 | HTTP and HTTPS for IoT | [View](notebooks/ch25-http-rest-webhooks-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch25-http-rest-webhooks-practice.ipynb) |
| 26 | IoT Communication Stack Selection Guide | [View](notebooks/ch26-protocol-selection-guide-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch26-protocol-selection-guide-practice.ipynb) |
| 27 | Microcontroller Programming and Deployment | [View](notebooks/ch27-microcontroller-programming-deployment-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch27-microcontroller-programming-deployment-practice.ipynb) |
| 28 | Thesis and Capstone Projects | [View](notebooks/ch28-project-planning-practice.ipynb) | [Run](https://colab.research.google.com/github/KuznetsovKarazin/fundamentals-of-iot-notebooks/blob/main/notebooks/ch28-project-planning-practice.ipynb) |

The [detailed index](docs/notebook-index.md) explains the link conventions, generated data, and chapter-specific setup. Chapter 10 preserves its established GitHub path, `ch10-common-iot-sensors-practice.ipynb`, so existing chapter links remain stable.

## Run locally

Clone or download the repository, then create an isolated Python 3.12 environment. Install the declared dependencies before opening a notebook:

```bash
git clone https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks.git
cd fundamentals-of-iot-notebooks
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Or in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install and start Jupyter:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

A Conda environment is also described in [`environment.yml`](environment.yml). Some setup cells may install a missing dependency; this requires network access. Restart the kernel and run all cells after changing dependencies.

## Validation

All **28 notebooks and 332 code cells** completed an independent sequential execution on 28 September 2026 with the recorded Python 3.12 environment. See [validation details](docs/validation.md) for the method, exact package versions, and limits. This check exercised notebook code in isolated IPython processes; it did not run the hosted Google Colab interface.

## Reproduce and extend

- Keep the notebook's initial seed and parameters for your baseline run. Change one assumption at a time and compare the resulting metrics and plots.
- Record the repository commit, Python/package versions, parameter changes, and any external inputs in your report. Fixed seeds alone do not guarantee identical results across every software version.
- Preserve the original notebook and work in your own copy. Several notebooks write CSV, JSON, or figure outputs to their working directory.
- Treat numerical models as teaching models. Hardware claims require physical measurements; a successful simulation is a different kind of evidence.

## Repository contents

| Location | Purpose |
|:--|:--|
| [`notebooks/`](notebooks/) | One main executable notebook per chapter |
| [`requirements.txt`](requirements.txt), [`environment.yml`](environment.yml) | Python dependencies |
| [`data/`](data/) | Data notes and companion teaching datasets |
| [`assets/`](assets/) | Supporting asset notes |
| [`docs/`](docs/) | Notebook index and distribution guidance |
| [`scripts/`](scripts/) | Notebook maintenance utilities |

## Cite and contribute

Please cite the textbook and identify the repository commit or release used in your work. [`CITATION.cff`](CITATION.cff) supplies repository citation metadata. Publication and archival metadata will be added when assigned.

For a reproducible issue report, include the chapter, failing cell, Python/package versions, complete error message, and whether you ran in Colab or locally. Suggestions that improve clarity, accessibility, and reproducibility are welcome.

## License

Companion code is covered by the [MIT License](LICENSE); companion instructional content is covered separately by [CC BY-NC 4.0](CONTENT_LICENSE.md), unless a file states otherwise. See [distribution and licensing scope](docs/distribution-and-licensing.md) for material outside this companion package.
