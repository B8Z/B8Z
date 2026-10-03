# A Genetic Algorithm for the Optimization of Service Provisioning in Multi-Layer Fog Networks

**Adam Bates · Christopher Newport University · Master's thesis, 2022**

[Original thesis listing on ProQuest](https://www.proquest.com/openview/492aa4a8f393f6e9388249c4cd0d7ba6/1?pq-origsite=gscholar&cbl=18750&diss=y)

**Portfolio note maintained October 3, 2026.** The date above belongs to the
original research. This note describes that work; it does not report a new
implementation or a reproduction of the original experiments.

## Problem

Service requests can require virtual network functions (VNFs) placed across
different layers of a fog network. A feasible placement must respect resource
capacity and delay constraints. Placement decisions interact: consuming capacity
for one request can change what remains feasible for another.

## Research contribution

The thesis developed a genetic algorithm and a VNF placement heuristic in Python,
using NumPy and NetworkX. It compared the approach with a Gurobi mixed-integer
linear programming model. The comparison asks how solution quality and runtime
vary with network, workload and resource-sharing configuration.

The tradeoff is configuration-dependent. A heuristic search and a mathematical
optimization model expose different choices in search budget, feasibility and
solution quality. This note makes no universal superiority claim and does not
attribute every comparison method to the thesis author.

## Reproduction status

The original source code, exact experiment configurations and result data are
not included in the currently reviewed public repositories. No 2026 reproduction
or newly timed experiment is claimed. Historical numerical results are not
repeated here without the original artifacts and their measurement context.

The linked thesis is the historical reference; its availability may depend on
ProQuest access. The listing could not be retrieved by the automated verification
tool during this portfolio update.

Running the original MILP comparison would require Gurobi and a license suitable
for the model size and use. Academic licenses have eligibility conditions;
restricted licenses have model-size limits. See
[Gurobi's academic licensing information](https://www.gurobi.com/academia/academic-program-and-licenses/).
No alternative solver has been substituted or described as the original comparison.

There is no runnable thesis example here until the original artifacts can be
checked. For a complete local engineering experiment requiring no commercial
solver or cloud service, see [Device Recovery Lab](https://github.com/B8Z/device-recovery-lab).

## What I would discuss in an interview

- How a placement heuristic handles capacity and delay feasibility.
- How the objective function and resource-sharing assumptions affect tradeoffs.
- Why a configured solver time limit must be distinguished from an observed
  runtime or a speedup claim.
- Why a fair comparison needs the same workload, constraints, objective,
  termination conditions and documented random seeds.

Those are methodological discussion points, not claims that new experiments have
been run. Restoring a reproducible research package is future work.
