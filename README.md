<picture>
  <source media="(max-width: 600px)" srcset="assets/hero-narrow.svg">
  <img src="assets/hero.svg" alt="Adam Bates, Senior Software Engineer focused on backend systems, integrations, and developer tooling.">
</picture>

I'm **Adam Bates, a senior software engineer** working on backend systems,
integrations, and developer tooling.

At JPMorgan Chase, I built Java/Spring Boot services for order management and
routing and independently implemented Kafka messaging. I built searchable
order auditing so engineers could follow a reported problem through the
sequence of events, and led a database migration to AWS with data validation
and a team-reviewed cutover after market close.

At Capital One, I joined without prior knowledge of the ATM architecture.
I learned how the application, vendor platform, host, and hardware worked
together, then used that understanding to lead technical work and independently
design and build a Python validation platform.

The platform gave engineering, product, legal, and hardware teams shared test
evidence. Visual and functional differences became structured defect reports
supporting reviewed fixes, rebuilding, and revalidation. I also set the
integration approach between the shared Vue.js library and ATM transaction
flows, so the UI team could keep developing its library while the ATM team
handled styling and kept the flows stable. The wider modernization remained
in progress when I left.

The connection between those roles is the kind of work I want to keep doing:
understanding how a system behaves, following problems across its boundaries,
and building software that makes it easier for other people to work with.

**Core stack:** Java, Spring Boot, Kafka, SQL, Python, and AWS.
My M.S. in Applied Physics and Computer Science also informs how I compare
alternatives and test what a result actually supports.

## Professional work

- [JPMorgan Chase: order routing, diagnostic evidence, and migration](professional/jpmorgan-chase.md)
- [Capital One: learning the system and making its behavior visible](professional/capital-one.md)

[Download the professional portfolio (PDF)](Adam-Bates_Engineering-Portfolio_Public.pdf).

These accounts separate my contribution, the team's work, and the limits of
the result. I'm happy to walk through the decisions behind either one.
[Connect with me on LinkedIn](https://www.linkedin.com/in/b8z/).

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
