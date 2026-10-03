# A Genetic Algorithm for the Optimization of Service Provisioning in Multi-Layer Fog Networks

**My master’s thesis · Christopher Newport University · 2022**

I developed a genetic algorithm and a virtual network function (VNF) placement
heuristic in Python, using NumPy and NetworkX, and compared the approach with a
Gurobi mixed-integer linear programming (MILP) model.

[Original thesis listing on ProQuest](https://www.proquest.com/openview/492aa4a8f393f6e9388249c4cd0d7ba6/1?pq-origsite=gscholar&cbl=18750&diss=y)

## The placement problem

A service request can require several VNFs placed across different layers of a
fog network. Each placement consumes capacity and contributes to delay, which
means a choice that works for one request can limit what remains feasible for
another. I examined this as a constrained optimization problem: the solution
must satisfy capacity and delay requirements as well as pursue the objective.

My implementation combined genetic search with a placement heuristic. The
comparison with the MILP model let me examine solution quality and runtime under
different network, workload, and resource-sharing configurations.

## How I interpret the comparison

The tradeoff depends on the configuration. A result for one workload and search
budget does not establish that a heuristic is always faster or produces better
solutions. Feasibility, solution quality, and runtime each need to be examined
under the same problem conditions.

A solver time limit sets a budget; it is not an observed runtime. I keep those
separate when interpreting the comparison. My contribution was the genetic
algorithm and placement heuristic; the MILP model provided the comparison.

## What is available here

**I updated this portfolio note on October 3, 2026. The research is from 2022.**
I haven’t reproduced the original experiments for this portfolio. The original
source, exact configurations, and result data are not included here, so I’m not
publishing new timings or repeating historical numbers without their experiment
context. The linked thesis is the historical reference; access may depend on
ProQuest.

Running the original MILP comparison requires Gurobi and a license suitable for
the model size and use. Academic licenses have eligibility requirements; see
[Gurobi’s licensing information](https://www.gurobi.com/academia/academic-program-and-licenses/).
I haven’t substituted another solver or described its output as the original
comparison.

A runnable research package would require checking the original artifacts and
documenting the workloads, constraints, objective, termination conditions, and
random seeds. That remains future work. For a complete experiment that runs
locally without a commercial solver, I’ve built
[Device Recovery Lab](https://github.com/B8Z/device-recovery-lab).

[Back to my profile](../README.md)
