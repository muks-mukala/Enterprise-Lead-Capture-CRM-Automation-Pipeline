"""
Data Cleaning & Sanitization Script for n8n Lead Ingestion Pipeline
Description: Parses raw incoming webhook payloads, sanitizes string fields,
and structures data for downstream CRM ingestion.
"""

def clean_incoming_leads(_input_data):
    output_items = []
    
    for item in _input_data.all():
        # Safely extract data whether nested under 'json' or passed directly
        data = item.get("json", item)
        body = data.get("body", data)
        
        email = str(body.get("email", "")).strip().lower()
        first_name = str(body.get("firstName", "Valued")).strip()
        last_name = str(body.get("lastName", "Lead")).strip()
        company = str(body.get("company", "Independent")).strip()
        message = str(body.get("message", "No message provided.")).strip()
        
        output_items.append({
            "json": {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "company": company,
                "message": message
            }
        })

    return output_items
