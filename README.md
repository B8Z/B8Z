# Adam Bates

**Senior Software Engineer · distributed services, device interfaces, and engineering tools**

I build services and interfaces that work across software and physical devices,
with testing, diagnostics, and recovery built into the engineering process.
My experience includes Java/Spring Boot and Kafka services at JPMorgan Chase,
customer-facing ATM interfaces and Python/Playwright automation at Capital One,
and NLP services at Width.ai.

Much of my professional work lives in proprietary employer repositories. These
public projects make my engineering approach inspectable through independent
implementations, explicit constraints, and reproducible evidence.

## Start here: [Device Recovery Lab](https://github.com/B8Z/device-recovery-lab)

**A message arrived. Did the locker open?** Request a simulated locker release,
inject a duplicate command, lose a completion acknowledgment, or disconnect the
device. Watch the service distinguish receipt from physical completion and
reconcile uncertainty without blindly repeating the action.

[![A real local run: the service is uncertain while the simulated device has performed one release pulse](https://raw.githubusercontent.com/B8Z/device-recovery-lab/main/docs/demo-uncertain.png)](https://github.com/B8Z/device-recovery-lab)

Open it for the [behavior contract](https://github.com/B8Z/device-recovery-lab/blob/main/docs/behavior.md),
[recovery controller](https://github.com/B8Z/device-recovery-lab/blob/main/lab/service.py),
and [tests and recorded observations](https://github.com/B8Z/device-recovery-lab/tree/main/measurements).
Two Python processes, HTTP, separate SQLite journals, and a small web interface;
runs locally without cloud services. This is a personal simulation, not an employer system.

## Complementary research

**[A Genetic Algorithm for the Optimization of Service Provisioning in Multi-Layer Fog Networks](research/fog-network-thesis.md)**
— master's thesis, Christopher Newport University, **2022**.

Python/NumPy/NetworkX research on genetic search and VNF placement under capacity
and delay constraints, with a Gurobi MILP comparison. Open the research note for
the problem, methods, configuration-dependent tradeoffs, and reproduction limits.
The original research date is distinct from this portfolio's October 2026 presentation.

[LinkedIn](https://www.linkedin.com/in/b8z/)
