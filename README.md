# Enterprise Lead-Capture & CRM Automation Pipeline
An automated, production-ready lead ingestion and synchronisation pipeline built with **n8n**, **Python**, **HubSpot CRM**, **Google Sheets**, and **Gmail**. This system eliminates manual data entry by securely capturing webhooks, sanitizing payloads, syncing records to a CRM, maintaining a real-time audit ledger, and dispatching instant notifications.

## Workflow Architecture
Webhook (JSON) ➔ Python (Data Cleaning & Validation) ➔ HubSpot CRM (Upsert Contact) ➔ Google Sheets (Master Audit Log) ➔ Gmail (Instant Alert)

## Key Features
* **Robust Webhook Ingestion:** Securely receives incoming lead data via active production endpoints.
* **Python Data Sanitisation:** Processes, cleans, and structures raw JSON payloads to prevent malformed data errors downstream.
* **HubSpot CRM Synchronisation:** Automatically creates or updates contact properties (First Name, Last Name, Email, Company) and retrieves CRM internal IDs.
* **Master Audit Trail:** Appends clean, formatted rows with precise UTC timestamps (`$now.toISO()`) into Google Sheets for permanent tracking.
* **Instant Email Notifications:** Dispatches customised, beautifully formatted lead alerts directly to the team inbox without external bloat.

## Tech Stack
* **Orchestration:** n8n (Self-Hosted / Cloud)
* **Data Processing:** Python (Pandas / Native JSON parsing)
* **CRM:** HubSpot API (v3 Contacts / Private Apps)
* **Storage & Auditing:** Google Sheets API
* **Communication:** Gmail API
