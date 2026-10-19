# Enterprise Lead-Capture & CRM Automation Pipeline
An automated, production-ready lead ingestion and synchronisation pipeline built with **n8n**, **Python**, **HubSpot CRM**, **Google Sheets**, and **Gmail**. This system eliminates manual data entry by securely capturing webhooks, sanitising payloads, syncing records to a CRM, maintaining a real-time audit ledger, and dispatching instant notifications.

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

## Setup & Configuration

If you want to deploy or test this workflow locally in your own n8n instance:

1. **Import the Workflow:** Download the JSON workflow template from this repo and import it into your self-hosted or cloud n8n instance.
2. **Configure Webhook:** Point your lead-capture web form to the Webhook node's production endpoint.
3. **Set Up Credentials:**
   * **HubSpot:** Connect your Private App API token with contact scope permissions.
   * **Google Sheets:** Authenticate via Google OAuth2 and link your master tracking sheet.
   * **Gmail:** Connect your sending account.
4. **Run Python Dependencies:** Ensure your n8n environment has access to standard Python execution libraries for the data-cleaning node.
5. **Activate:** Toggle the workflow status to **Published** for 24/7 automated processing.

### Key Results & Business Impact
* **Eliminated Manual Overhead:** Reduced lead processing time from hours to milliseconds with 100% automated end-to-end routing.
* **Guaranteed Data Hygiene:** Prevented bad payloads and malformed inputs from breaking downstream CRM records using robust Python validation.
* **Real-Time Visibility:** Provided immediate stakeholder awareness via instant email alerts while maintaining a clean, permanent audit trail in Google Sheets.
