<picture>
  <source media="(max-width: 600px)" srcset="assets/hero-narrow.svg">
  <img src="assets/hero.svg" alt="Adam Bates, Senior Software Engineer focused on backend systems, integrations, and developer tooling.">
</picture>

I'm **Adam Bates, a senior software engineer focused on backend systems,
integrations, and developer tooling**.

**Core stack:** Java, Spring Boot, Kafka, SQL, Python, and AWS.

## Professional background

At **JPMorgan Chase**, I built Java/Spring Boot services for order management
and routing, independently implemented Kafka messaging, and built an order-audit
system that made bugs easier to identify. I also led an order-management
database migration to AWS, validating the data and coordinating the cutover
with the team.

At **Capital One**, I led the ATM interface modernization team's technical
work, built the customer interface, and independently developed Python-based
validation tooling for QA hardware. I worked with engineers and vendors to
diagnose problems across application, host, and hardware boundaries. Earlier,
I led Python and NLP development at **Width.ai**.

My M.S. in **Applied Physics and Computer Science** informs how I define
constraints, compare alternatives, and test what a result actually supports.

I'm interested in backend and integration engineering, modernization, and
tools that help engineering teams diagnose problems and deliver dependable
software. [Connect with me on LinkedIn](https://www.linkedin.com/in/b8z/).

Read the professional case studies: [JPMorgan Chase backend and integration](professional/jpmorgan-chase.md)
· [Capital One validation and developer tooling](professional/capital-one.md).

## Selected independent projects

These projects show how I investigate failures, make design decisions, and
verify results. They are independent implementations, separate from employer
systems.

### Device Recovery Lab

Reliable command processing requires more than receiving a message. I built
separate service and simulated-device processes with durable journals to
explore duplicate delivery, lost completion responses, and recovery. The
service inspects journal evidence before deciding whether to retry; unresolved
physical outcomes require inspection. This is a simulation, not a claim of
exactly-once physical execution or power-loss safety.

[Explore the recorded timeline](https://b8z.github.io/device-recovery-lab/)
· [Read the code and run it locally](https://github.com/B8Z/device-recovery-lab)
· [Inspect the crash tests](https://github.com/B8Z/device-recovery-lab/blob/main/tests/test_crash_boundary.py)

### Placement Tradeoffs

I compare greedy placement and seeded genetic search against exhaustive
enumeration under shared capacity, deadline, and cost constraints. The
experiments expose assignments and the gap from the optimum, so the result
can be assessed against its configuration and search budget.

This is an independent October 2026 implementation. My 2022 master's thesis
addressed a richer fog-network placement problem; it is separate research.
[Read my thesis note](research/fog-network-thesis.md).

[Explore the recorded experiments](https://b8z.github.io/placement-tradeoffs/)
· [Read the model and run it locally](https://github.com/B8Z/placement-tradeoffs)
· [Inspect the measurements](https://github.com/B8Z/placement-tradeoffs/tree/main/measurements)

---

Both viewers show recorded output from local runs. Each repository also starts
with `python run.py` for fresh experiments without a cloud account. I use AI
assistance and verify the work through explicit behavior contracts, tests,
and reproducible experiments. [How the illustrations are made](art/README.md).
