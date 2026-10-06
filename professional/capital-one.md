# Capital One validation and developer tooling

Adam Bates | Senior Software Engineer, Bank Tech | February 2025 - August 2026

I independently designed and built a Python-based validation platform for ATM software on QA hardware. It brought functional checks, design comparisons, remediation reports, and an enterprise dashboard into one workflow, giving engineers and partner teams a shared view of the implemented customer journeys.

## Problem and responsibility

The modernization crossed application, host, vendor, and hardware boundaries. Product, design, legal, hardware, and engineering teams needed to understand the same behavior, but their responsibilities and constraints differed.

The project was assigned to me. I determined its architectural approach while working with external teams and conflicting interests. I also led the interface modernization team's technical work and implemented the customer interface. The wider ATM team retained responsibility for the overall software, releases, and operations.

## Implementation and validation

I used Python and Playwright to automate functional and visual checks against QA hardware. A run followed the implemented, reachable customer flows, collected test evidence, compared screens with the intended designs, and produced reports that engineers could use to investigate defects.

The dashboard brought those results together so teams could inspect the same behavior and evidence. The reports helped connect a visible failure to the relevant application, host, hardware, or vendor layer. Proposed code changes went through review, rebuilding, and revalidation; producing a report did not mean a fix had been deployed.

Separately, I built reusable JUnit infrastructure and shared checks that expanded unit-test coverage of custom ATM code. Those checks ran in the team's existing pipeline. I did not create or replace that pipeline.

## Result and scope

The validation platform automated checks and reporting for the customer flows implemented at the time. It helped other teams understand functionality and gave engineers concrete evidence for remediation. Shared JUnit checks also brought broader unit-test coverage into the existing delivery process.

The overall interface modernization remained in progress when I left. The tooling's coverage was bounded by the implemented, reachable scenarios, and its visual accessibility checks did not establish complete accessibility compliance. Validation, code remediation, and production release remained distinct steps.
