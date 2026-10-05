<picture>
  <source media="(max-width: 600px)" srcset="assets/engineering-mobile.svg">
  <img src="assets/engineering.svg" alt="Adam Bates — Senior Software Engineer. Complex systems, optimization, and technical leadership. I build and improve complex systems, and help teams understand them.">
</picture>

I’m **Adam Bates, a Senior Software Engineer** with 7+ years across software
development and applied research. I build and improve complex systems, from
financial applications and customer-facing interfaces to the tools engineers
use to test, diagnose, and maintain them.

I take ownership from understanding the problem through implementation and
validation. That includes working through unfamiliar parts of a system,
weighing trade-offs, and helping the team understand the decisions.

At **JPMorgan Chase**, I implemented Kafka messaging for a Java/Spring Boot
trade-routing platform, built order-lifecycle auditing, and led a database
migration to AWS. At **Capital One**, I led the ATM interface modernization
team, built customer-facing interfaces, and independently developed Python-based
automation to validate software on QA hardware. I also worked with engineers
and vendors to diagnose problems across application, host, and hardware boundaries.

Earlier, I built Python NLP services at **Width.ai**. My master’s research in
**Applied Physics and Computer Science** focused on algorithmic optimization
under capacity and delay constraints.

Much of my professional work lives in proprietary employer repositories.
These independent projects let me show the decisions, tests, and experiments
behind my engineering without publishing employer systems.

## Two ways to inspect my work

| Project | Start here | What to look for |
| --- | --- | --- |
| **[Device Recovery Lab](https://github.com/B8Z/device-recovery-lab)** | [Break communication, inspect recovery →](https://b8z.github.io/device-recovery-lab/) | How I protect correctness across service/device boundaries, test recovery independently, and evaluate concurrency under faults. |
| **[Placement Tradeoffs](https://github.com/B8Z/placement-tradeoffs)** | [Explore recorded experiments →](https://b8z.github.io/placement-tradeoffs/) | How I define an optimization objective, preserve constraints, compare algorithms fairly, and explain when a simpler method is enough. |

Both browser viewers show **recorded output from real local runs**. Each
repository also starts with `python run.py` for live experiments, without a cloud
account or runtime package installation.

### 01 / Device Recovery Lab

**The door opened. The reply didn’t.**

[![The door opened, but its reply was lost. A captured simulator run shows one physical action while the service remains uncertain; guided recovery checks the controller evidence.](https://raw.githubusercontent.com/B8Z/device-recovery-lab/main/docs/experiment-workbench.png)](https://b8z.github.io/device-recovery-lab/)

I built a parcel-locker simulator with separate service and device processes,
durable journals, and a visible event timeline. Introduce duplicate delivery,
lose a completion response, or disconnect the device and restore its link.
The recovery controller queries the execution journal before deciding to resend.
The illustration follows captured observations; the local lab runs the processes.

Then I remove the assumption that makes reconciliation possible: terminate the
actual controller process before or after a pulse, while completion is still
unrecorded. Both restarted journals report the same uncertainty. One locker has
acted; the other has not. The service preserves that uncertainty and requires
inspection because retrying would risk repeating a completed action.

I also compare one and four recovery workers under identical queued workloads,
with faults injected by a separate HTTP proxy. Durable claims prevent stale
workers from overwriting newer decisions. The tests kill the service during an
outstanding response and reject a deliberately broken worker that claims success
without completion evidence.

In the [recorded experiment](https://github.com/B8Z/device-recovery-lab/blob/main/docs/workload.md),
all 864 measured operations passed the recorded invariants. Four workers reduced
the typical completion time, but one mixed-fault batch was slower with four.
I keep that exception visible because the experiment supports a conditional
result, not a universal speedup.

**Inspect:** [expected behavior](https://github.com/B8Z/device-recovery-lab/blob/main/docs/behavior.md)
· [recovery controller](https://github.com/B8Z/device-recovery-lab/blob/main/lab/service.py)
· [process-crash tests](https://github.com/B8Z/device-recovery-lab/blob/main/tests/test_crash_boundary.py)
· [worker ownership tests](https://github.com/B8Z/device-recovery-lab/blob/main/tests/test_ownership.py)
· [matched workloads and the slower run](https://b8z.github.io/device-recovery-lab/#workload)

The diagnostic device panel can see behind a broken link; the service cannot use
that panel as completion evidence. These are synthetic correctness experiments;
they do not establish exactly-once physical execution or power-loss safety.

### 02 / Placement Tradeoffs

**A placement can be feasible and still block a better combination.**

[![Actual solver output: greedy scores 23 while genetic search and exhaustive enumeration reach 27 under tight deadlines. The placement map shows capacity use and the search trace.](https://raw.githubusercontent.com/B8Z/placement-tradeoffs/main/docs/placement-comparison.png)](https://b8z.github.io/placement-tradeoffs/)

I compare greedy placement, seeded genetic search, and an exhaustive reference
on the same small model. Change capacity, deadlines, or cost, then inspect the
admitted requests, rejected requests, capacity use, and objective gap.

In the [recorded experiment](https://github.com/B8Z/placement-tradeoffs/tree/main/measurements),
greedy reaches the optimum in three configurations. Under tighter deadlines it
scores 23 against an optimum of 27; genetic search reaches 27 in the five tested
seeds. I retain the inputs, timings, variability and source revision so the
tradeoff can be checked rather than generalized from a headline.

**Inspect:** [model contract](https://github.com/B8Z/placement-tradeoffs/blob/main/docs/contract.md)
· [three solvers](https://github.com/B8Z/placement-tradeoffs/blob/main/placement/solvers.py)
· [hand-solved correctness checks](https://github.com/B8Z/placement-tradeoffs/blob/main/tests/test_placement.py)

This is a new October 2026 implementation. My **2022 master’s thesis at Christopher
Newport University** addressed a richer VNF-placement problem with Python, NumPy,
NetworkX and a Gurobi MILP comparison. I keep the historical research and current
experiments separate: [read my thesis note](research/fog-network-thesis.md).

## How I approach the work

Before optimizing a system, I establish what we’re trying to improve and what
needs to stay intact. That might mean reducing execution time, resource use, or
manual effort while preserving correctness. I use focused experiments to check
whether a change helps under the conditions that matter, and keep the limitations
visible so the next decision has a useful starting point.

I also make the reasoning available to the people maintaining the system through
technical guidance, documentation, and mentoring.

## What I’m looking for

I’m interested in **senior software engineering and hands-on technical lead
roles**, particularly in backend and platform engineering, modernization,
integration, and developer tooling. I’m open to different domains where I can
help shape technical decisions while staying involved in implementation.

## How I use tools and evidence

I use AI assistance in these projects. The useful part is what I can verify:
an explicit behavior contract, a small reproducible case, and results that retain
their workload and measurement conditions. A passing test supports the behavior
it exercised; a simulation result stays a simulation result.

[LinkedIn](https://www.linkedin.com/in/b8z/) ·
[Recovery lab](https://github.com/B8Z/device-recovery-lab) ·
[Placement experiment](https://github.com/B8Z/placement-tradeoffs)
