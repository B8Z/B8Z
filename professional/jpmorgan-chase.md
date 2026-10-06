# JPMorgan Chase backend and integration work

Adam Bates | Software Engineer I / II, Asset & Wealth Management | February 2022 - February 2025

I built Java/Spring Boot services for order management and routing, independently implemented Kafka messaging within the trade-routing platform, and built its order-audit system. My work connected service behavior, diagnostic evidence, and production validation so the team could understand how an order moved through the system and investigate problems more effectively.

## Responsibility and collaboration

I implemented the Kafka messaging that replaced the internal routing mechanism. Topic, key, and partition design involved a more senior developer, and some logic was pair-programmed. My services handled order management and routing within a broader financial platform; other teams and engineers owned the surrounding capabilities.

I also built the order-audit system end to end with Spring Boot, SQL, Liquibase, and documented APIs searchable by field. The append-only history supported engineering investigations as well as compliance and audit requests.

## Decisions and validation

The routing change introduced asynchronous processing while retaining the existing order-state logic. I implemented idempotent consumers, per-order ordering, locking, and replay handling to prevent a retried message from processing an order twice. Those mechanisms addressed the application's order-processing behavior; they are not a claim that every external action can happen exactly once.

I built end-to-end order-lifecycle tests using Groovy, JUnit, and Mockito. I also partnered with another team's lead on performance testing during the Kafka upgrade. Production releases took place after Friday market close, with failover checks and monitoring through Splunk and Datadog.

Separately, I led an order-management database migration to AWS. I kept the source and destination synchronized, converted the schema and database-specific SQL, and validated the migrated data. The team reviewed the cutover plan before the move after market close.

## Result and scope

After the Kafka upgrade, the platform had fewer failures and was easier to investigate. The audit system made bugs faster to identify by preserving the sequence of order events. The database migration completed without downtime during trading hours and improved cost, reliability, and security.

These are descriptions of my contribution within the team's platform. They do not imply ownership of the entire trading system, and the performance-testing work has no separately recorded result to claim.
