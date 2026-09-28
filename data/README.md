# Dataset provenance

These companion data support the educational computations in the 28 notebooks. **Most are synthetic or model-generated.** They are not a collection of physical IoT deployment measurements.

The core exercises generate their data locally and require no external research dataset download. For most chapters, the reproducible data definition is the notebook code and its declared inputs/seeds; this package does not duplicate all notebook code or export every temporary array.

## Chapter coverage

| Chapter | Origin and interpretation |
|---:|---|
| 1 | Synthetic 12-sample temperature stream, UTC telemetry table and threshold flags; seed 42. |
| 2 | Five author-created IoT planning scenarios, configuration-driven record/payload estimates and modified-interval comparison; no deployment measurements. |
| 3 | Synthetic single-device daily telemetry, seeded incomplete fleet records, and an author-defined system-boundary classification matrix. |
| 4 | Synthetic room context, simplified thermal-control responses, service availability/latency draws, and adaptive preference-policy scenarios. |
| 5 | Author-declared device state currents/durations; synthetic event arrivals and response delays; synthetic solar/cloud week and RTOS task workloads. |
| 6 | Synthetic protocol-register examples, mixed gateway workloads, sklearn-generated classification data and architectural WAN/outage assumptions; fault/failover simulations. |
| 7 | Synthetic bursty fleet arrivals, connectivity/desire-state events, matched OTA campaign scenarios, and multi-tenant workloads. |
| 8 | Synthetic waste generation/routes, manufacturing faults, street-light usage and physiological-score monitoring. The physiological score has no clinical interpretation. |
| 9 | Simulated measurement chains, transfer characteristics, step/frequency responses, and noisy samples for bias/precision/resolution/sensitivity analysis. |
| 10 | Simulated temperature networks, environmental temperature/pressure, inertial sensor fusion signals, and humidity-sensor behaviour. |
| 11 | Synthetic spectra and mixtures, gas-sensor calibration/cross-sensitivity, synthetic biometric genuine/impostor scores and simulated environmental events; no personal biometric records. |
| 12 | Numerical solenoid/motor/control/actuator models and generated state trajectories; mostly deterministic ODE/discrete simulations. |
| 13 | Constructed sampled signals, quantization and anti-aliasing models, plus seeded clock-jitter Monte Carlo trials. |
| 14 | Shared synthetic sensor signals for filtering, injected transient outliers, compression and feature-extraction windows. |
| 15 | Computed I2C/SPI/UART timing and transaction sequences, simulated bus failures/retries and clock/synchronisation traces. |
| 16 | Synthetic calibration points, drift/fault simulations and vibration-degradation trajectories; fitted prediction and bootstrap analyses operate on those generated data. |
| 17 | Illustrative technology range/rate/power intervals and calculated representative points; path-loss, capacity and energy model curves. These are not measured product benchmarks. |
| 18 | Modelled Wi-Fi link adaptation/CSMA and BLE connection/channel scenarios; seeded contention/interference Monte Carlo checks. |
| 19 | Synthetic mesh topology/link metrics, routing/hop analyses, failure/reselection Monte Carlo scenarios and technology comparison models. |
| 20 | Modelled LoRaWAN/Sigfox propagation, airtime, traffic/energy and independent-transmission reliability; generated Monte Carlo validation samples. |
| 21 | Published NB-IoT measured energy constants and source-attributed planning parameters embedded in code, followed by derived battery/link/rate curves and synthetic NPRACH collision trials. No source raw measurement dataset is redistributed. |
| 22 | Constructed MQTT packet/topic/subscription data, simulated loss/QoS and offline-session arrivals; local topic-trie versus naive-scan timing is a software microbenchmark and varies by environment. |
| 23 | Constructed industrial protocol frames and synthetic change/queueing/loss scenarios; illustrative installation and decision parameters. |
| 24 | Constructed CoAP/HTTP framing plus seeded exchange-loss, Observe lifecycle and blockwise-transfer simulations. |
| 25 | Synthetic telemetry entropy scenarios and event traces; real local serialization/HMAC/JWT computations and timing, plus modelled network setup/RTT/rate-limit/webhook behaviour. Ephemeral token values may vary by run. |
| 26 | Author-selected technology/stack/catalogue scores, constraints, energy/cost parameters and uncertain preference draws; teaching assumptions, not vendor benchmark constants. |
| 27 | Deterministic resource-screen, job-scheduler and quantized-LUT tables. Exercise 27.3 paired speedups are explicitly pedagogical synthetic values constrained by published error bounds, not raw simulator or hardware observations. |
| 28 | Author-created capstone project catalogue with illustrative 1-5 scores, experiment budgets, milestones and readiness values; planning estimates, not research results. |

## Included small files

All files below are byte-identical copies from the source package. SHA-256 hashes, CSV row counts and columns are recorded in `dataset-provenance.json`.

| File | Rows | Status |
|---|---:|---|
| `chapter_02/data/iot_project_scenarios.csv` | 5 | author-created synthetic teaching input |
| `chapter_02/config/project_config.json` | - | author-created synthetic teaching input |
| `chapter_02/outputs/scenario_summary.csv` | 5 | archived derived teaching output or provenance/configuration; original environment snapshot, not current audit run |
| `chapter_02/outputs/modified_scenario_summary.csv` | 5 | archived derived teaching output or provenance/configuration; original environment snapshot, not current audit run |
| `chapter_02/outputs/modified_config.json` | - | archived derived teaching output or provenance/configuration; original environment snapshot, not current audit run |
| `chapter_02/outputs/environment_manifest.json` | - | archived derived teaching output or provenance/configuration; original environment snapshot, not current audit run |
| `chapter_02/outputs/comparison_manifest.json` | - | archived derived teaching output or provenance/configuration; original environment snapshot, not current audit run |
| `chapter_27/data/exercise_27_1_resource_feasibility.csv` | 30 | deterministic model output; not physical measurements |
| `chapter_27/data/exercise_27_2_scheduler_sweep.csv` | 34 | deterministic model output; not physical measurements |
| `chapter_27/data/exercise_27_3_pedagogical_agreement_data.csv` | 14 | pedagogical synthetic paired values or their derived summary; NEVER raw hardware evidence |
| `chapter_27/data/exercise_27_3_pedagogical_agreement_summary.csv` | 2 | pedagogical synthetic paired values or their derived summary; NEVER raw hardware evidence |
| `chapter_27/data/exercise_27_4_lut_pareto.csv` | 12 | deterministic model output; not physical measurements |
| `chapter_27/data/exercise_27_4_lut_sweep.csv` | 18 | deterministic model output; not physical measurements |
| `chapter_27/environment_manifest.json` | - | archived reference software environment; not a dataset or physical measurement |
| `chapter_28/project_candidates.csv` | 12 | illustrative project-planning catalogue; subjective planning estimates |

## Critical interpretation notes

- Chapter 27 Exercise 27.3 has 14 deterministic synthetic pairs. The fields named `simulator_speedup` and `hardware_speedup` do **not** make them physical observations. The summary CSV is derived from those same synthetic pairs. Reproduction of the published experiment requires separate raw logs, firmware/toolchain information and a measurement protocol.

- Chapter 21 combines published empirical aggregate constants with model assumptions. The principal measured-energy source is [Michelinakis et al.](https://doi.org/10.1109/JIOT.2020.3013949). The 10 microwatt PSM value is a rounded representative value, not an exact reported median. No original measurement traces are included.

- Chapters 22 and 25 include local software timing measurements. Their timings vary with the interpreter, package versions, hardware and system load. Network RTT/handshake parameters and generated event traces remain model inputs.

- Chapter 28 mentions possible future research datasets (for example, an IDS benchmark or licensed biometric datasets) as project suggestions. Such datasets are not part of this archive and their original access/license conditions still apply.

- Chapter 2 provenance JSON and Chapter 27 environment JSON describe the archived source environments. They are retained as historical provenance and should not be relabelled as the environment of a new run.

## Use and regeneration

Open the matching notebook from [the companion repository](https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks). Restart its kernel/runtime and run all cells in order. Chapter 2 and Chapter 28 bootstrap their small editable input files when those files are absent. Chapter 27 uses the same executable core as its source archive. Keep units, parameters, seeds, source/version and environment information with any regenerated outputs. Consult the notebook and book for model boundaries and interpretation.

This package deliberately excludes manuscript text, book figures, assessment answers and third-party raw research datasets. Existing simulator wiring JSON is code support rather than a dataset.

## Repository navigation

The [notebook index](../docs/notebook-index.md) links to all 28 chapter notebooks. In `dataset-provenance.json`, `notebook` values are relative to the repository root, while `packaged_files.path` values are relative to this `data/` directory. Original-source names identify the supplied archive and need not match normalized repository filenames.
