# Package contents

The companion package contains **28 main Jupyter notebooks**, mapped to the current textbook chapters in the [notebook index](docs/notebook-index.md).

## Main notebooks

| Chapter | File |
|:--|:--|
| 01 | [`ch01-first-steps-python-colab.ipynb`](notebooks/ch01-first-steps-python-colab.ipynb) |
| 02 | [`ch02-reproducible-python-project.ipynb`](notebooks/ch02-reproducible-python-project.ipynb) |
| 03 | [`ch03-defining-iot-practice.ipynb`](notebooks/ch03-defining-iot-practice.ipynb) |
| 04 | [`ch04-fundamental-iot-concepts-paradigms-practice.ipynb`](notebooks/ch04-fundamental-iot-concepts-paradigms-practice.ipynb) |
| 05 | [`ch05-iot-device-technologies-practice.ipynb`](notebooks/ch05-iot-device-technologies-practice.ipynb) |
| 06 | [`ch06-iot-gateways-edge-processing-practice.ipynb`](notebooks/ch06-iot-gateways-edge-processing-practice.ipynb) |
| 07 | [`ch07-iot-platforms-practice.ipynb`](notebooks/ch07-iot-platforms-practice.ipynb) |
| 08 | [`ch08-iot-impact-industry-society-practice.ipynb`](notebooks/ch08-iot-impact-industry-society-practice.ipynb) |
| 09 | [`ch09-fundamentals-sensor-technology-practice.ipynb`](notebooks/ch09-fundamentals-sensor-technology-practice.ipynb) |
| 10 | [`ch10-common-iot-sensors-practice.ipynb`](notebooks/ch10-common-iot-sensors-practice.ipynb) |
| 11 | [`ch11-advanced-sensor-technologies-practice.ipynb`](notebooks/ch11-advanced-sensor-technologies-practice.ipynb) |
| 12 | [`ch12-actuators-control-practice.ipynb`](notebooks/ch12-actuators-control-practice.ipynb) |
| 13 | [`ch13-data-acquisition-practice.ipynb`](notebooks/ch13-data-acquisition-practice.ipynb) |
| 14 | [`ch14-onboard-data-processing-practice.ipynb`](notebooks/ch14-onboard-data-processing-practice.ipynb) |
| 15 | [`ch15-sensor-actuator-integration-practice.ipynb`](notebooks/ch15-sensor-actuator-integration-practice.ipynb) |
| 16 | [`ch16-sensor-calibration-maintenance-practice.ipynb`](notebooks/ch16-sensor-calibration-maintenance-practice.ipynb) |
| 17 | [`ch17-wireless-overview-practice.ipynb`](notebooks/ch17-wireless-overview-practice.ipynb) |
| 18 | [`ch18-wifi-bluetooth-practice.ipynb`](notebooks/ch18-wifi-bluetooth-practice.ipynb) |
| 19 | [`ch19-mesh-networks-practice.ipynb`](notebooks/ch19-mesh-networks-practice.ipynb) |
| 20 | [`ch20-lpwan-practice.ipynb`](notebooks/ch20-lpwan-practice.ipynb) |
| 21 | [`ch21-cellular-iot-practice.ipynb`](notebooks/ch21-cellular-iot-practice.ipynb) |
| 22 | [`ch22-mqtt-practice.ipynb`](notebooks/ch22-mqtt-practice.ipynb) |
| 23 | [`ch23-wired-industrial-practice.ipynb`](notebooks/ch23-wired-industrial-practice.ipynb) |
| 24 | [`ch24-coap-practice.ipynb`](notebooks/ch24-coap-practice.ipynb) |
| 25 | [`ch25-http-rest-webhooks-practice.ipynb`](notebooks/ch25-http-rest-webhooks-practice.ipynb) |
| 26 | [`ch26-protocol-selection-guide-practice.ipynb`](notebooks/ch26-protocol-selection-guide-practice.ipynb) |
| 27 | [`ch27-microcontroller-programming-deployment-practice.ipynb`](notebooks/ch27-microcontroller-programming-deployment-practice.ipynb) |
| 28 | [`ch28-project-planning-practice.ipynb`](notebooks/ch28-project-planning-practice.ipynb) |

## Supporting files

| File or directory | Role |
|:--|:--|
| `README.md` | Quick start, learning tracks, chapter links, and local execution |
| `notebooks/README.md` | Notebook workflow and stable-filename conventions |
| `docs/notebook-index.md` | Full index, setup notes, and data provenance guidance |
| `docs/validation.md` | Execution method, environment, results, and limitations |
| `docs/distribution-and-licensing.md` | Scope of companion distribution and licenses |
| `requirements.txt`, `environment.yml` | Python dependency declarations |
| `scripts/clean_notebooks.py` | Utility for removing saved notebook outputs |
| `.github/workflows/notebook-smoke-test.yml` | Automated notebook execution workflow |
| `data/` | 15 small source CSV/JSON files, chapter-by-chapter dataset provenance, file hashes and interpretation notes |
| `assets/` | Supporting-asset documentation |
| `CITATION.cff` | Repository citation metadata |
| `LICENSE`, `CONTENT_LICENSE.md` | Existing code and educational-content licenses |
| `.gitignore`, `.gitattributes` | Repository maintenance settings |

The notebooks include or generate the inputs needed for their core exercises. See chapter-specific notes before reusing generated data. The manuscript, chapter PDFs, instructor slide decks, private correspondence, and publisher files are outside this package.

## Teaching datasets

See [data/README.md](data/README.md) for all 28 chapters and the 15 included source files. Most examples use synthetic data or deterministic models; Chapter 21 also uses published aggregate energy constants, and Chapters 22/25 include local software timing. Chapter 27 Exercise 27.3 is explicitly synthetic and is not hardware evidence. The data package contains no instructor assessment answers.
