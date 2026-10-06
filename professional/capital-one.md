# Capital One: learning the system and making its behavior visible

Adam Bates | Senior Software Engineer, Bank Tech | February 2025 - August 2026

I joined Capital One without prior knowledge of its ATM architecture. I learned how the application, vendor platform, host, and hardware worked together, then used that understanding to lead the interface modernization team's technical work and independently design and build a Python validation platform.

The useful part of that knowledge was being able to explain what the system was doing and give other people a way to inspect it themselves.

## Understanding the system

A customer journey crossed several systems and team boundaries. Understanding the interface meant understanding the transaction flow behind it, the host's behavior, and what happened at the device. I diagrammed transaction flows and architecture, investigated ATM journals, and worked with vendors and internal teams to trace problems across those boundaries.

In separate production incident work, I traced a reboot loop across application, host, device, and vendor layers and drove root-cause fixes with the teams involved. I also helped the modernization team learn the architecture as I directed its technical work.

## Turning that understanding into a tool

Product, design, legal, hardware, and engineering teams had different responsibilities and constraints. The validation project was assigned to me; I determined its architecture independently while working with those teams. The platform gave them a shared view of how the implemented customer journeys behaved.

I used Python and Playwright to run functional and visual checks on QA hardware. A run followed reachable customer flows, collected evidence, compared screens with their intended designs, and produced flow maps and remediation reports. The dashboard brought those outputs together for engineers and partner teams.

This made the behavior inspectable beyond my own explanation of it. Engineers could use the evidence to investigate defects, while other teams could understand the functionality relevant to their work. Proposed fixes still went through review, rebuilding, and revalidation.

## Contribution and outcome

I independently designed and built the validation tooling. I also led the interface modernization team's technical work and implemented the customer interface, integrating a shared Vue.js library with the vendor platform. Other engineers built that library, and the wider ATM team owned releases and operations.

The platform automated validation and reporting for the implemented, reachable scenarios and helped other teams understand the software. The overall modernization remained in progress when I left. Visual checks did not establish complete accessibility compliance, and a successful validation run did not mean a production release had occurred.
