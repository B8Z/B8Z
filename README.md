<picture>
  <source media="(max-width: 600px)" srcset="assets/hero-narrow.svg">
  <img src="assets/hero.svg" alt="Adam Bates — Senior Software Engineer. I build and improve complex systems, and help teams understand them. Financial systems, device integration, and applied optimization.">
</picture>

I’m a **Senior Software Engineer with 7+ years across software development and
applied research**. My work spans financial applications, customer-facing
interfaces, hardware integration, and the tools engineers use to understand
and maintain them. I take ownership from figuring out the problem through
implementation and validation, and help the team understand the decisions.

Much of my professional work lives in proprietary employer repositories.
These independent projects show how I work through failure, test an explanation,
and evaluate a trade-off.

**Start here:** [Recovery under failure](https://b8z.github.io/device-recovery-lab/)
· [Optimization experiments](https://b8z.github.io/placement-tradeoffs/)
· [Professional background](#professional-background)
· [LinkedIn](https://www.linkedin.com/in/b8z/)

## Device Recovery Lab

<a href="https://b8z.github.io/device-recovery-lab/">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/plate-recovery-narrow.svg">
    <img src="assets/plate-recovery.svg" alt="Two illustrated controller-crash outcomes from the lab: before the pulse, the simulated locker is closed with zero physical pulses; after the pulse, it is open with one. Both controller journals say IN_DOUBT. Open the recorded viewer to inspect the evidence.">
  </picture>
</a>

**Receiving a command doesn’t establish that the physical action completed.**
I built separate service and device processes with durable journals, then tested
duplicate delivery, a lost completion response, and a device that reconnects.
The service queries the device’s execution journal before deciding to resend.

The harder case is a controller crash before completion is recorded. I terminate
the actual process on either side of the simulated physical pulse. Both restarted
journals report `IN_DOUBT`, although only one locker acted. The service requires
inspection because it cannot safely infer which outcome occurred.

[Explore the recorded timeline →](https://b8z.github.io/device-recovery-lab/)
· [Read the code and run it locally](https://github.com/B8Z/device-recovery-lab)
· [Inspect the crash tests](https://github.com/B8Z/device-recovery-lab/blob/main/tests/test_crash_boundary.py)

I also compare one and four recovery workers under matched workloads.
The [measurement report](https://github.com/B8Z/device-recovery-lab/blob/main/docs/workload.md)
includes all 864 measured operations and the mixed-fault batch that was slower
with four workers. These are synthetic experiments, not a claim of exactly-once
physical execution or power-loss safety.

## Placement Tradeoffs

<a href="https://b8z.github.io/placement-tradeoffs/">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/plate-placement-narrow.svg">
    <img src="assets/plate-placement.svg" alt="Illustration of the tighter-deadline fixture. Only Edge is eligible, with six capacity units. Greedy places C in five units for objective 23. Genetic search and exhaustive enumeration place D and E in six units for objective 27. Open the recorded experiments.">
  </picture>
</a>

**A feasible choice can leave less room for a better combination.** I compare
greedy placement, seeded genetic search, and exhaustive enumeration on the same
small model. The viewer exposes assignments, rejected requests, capacity use,
and the gap from the optimum.

In the recorded experiment, greedy reaches the optimum in three configurations.
With tighter deadlines it scores 23 against an optimum of 27; genetic search
reaches 27 in the five tested seeds. The result depends on the configuration
and search budget.

[Explore the recorded experiments →](https://b8z.github.io/placement-tradeoffs/)
· [Read the model and run it locally](https://github.com/B8Z/placement-tradeoffs)
· [Inspect the measurements](https://github.com/B8Z/placement-tradeoffs/tree/main/measurements)

This is a new October 2026 implementation. My **2022 master’s thesis at
Christopher Newport University** addressed a richer VNF-placement problem with
Python, NumPy, NetworkX, and a Gurobi MILP comparison. I keep the original research
separate from these new experiments: [read my thesis note](research/fog-network-thesis.md).

## Professional background

At **JPMorgan Chase**, I implemented Kafka messaging for a Java/Spring Boot
trade-routing platform, built order-lifecycle auditing, and led a database
migration to AWS.

At **Capital One**, I led the ATM interface modernization team, built
customer-facing interfaces, and independently developed Python-based automation
to validate software on QA hardware. I worked with engineers and vendors to
diagnose problems across application, host, and hardware boundaries. Earlier,
I built Python NLP services at **Width.ai**.

My master’s background in **Applied Physics and Computer Science** informs how
I approach optimization: establish the objective and constraints, compare under
the same conditions, and check what the result actually supports. I make that
reasoning available through technical guidance, documentation, and mentoring.

I’m interested in **senior engineering and hands-on technical lead roles** in
backend and platform engineering, modernization, integration, and developer
tooling, including opportunities in other domains with these kinds of problems.
[Connect with me on LinkedIn](https://www.linkedin.com/in/b8z/).

---

Both viewers show recorded output from real local runs; each repository also
starts with `python run.py` for fresh experiments without a cloud account.
I use AI assistance in these projects and verify the work through explicit
behavior contracts, tests, and reproducible experiments.
[How the illustrations are made](art/README.md).
