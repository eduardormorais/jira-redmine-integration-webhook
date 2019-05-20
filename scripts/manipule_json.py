import json

def get_fields_values(webhook_json):
    val = webhook_json
    issue = val['payload']['issue']
    custom_fields = issue['custom_field_values']
    summary = issue['subject']
    description = issue['description']
    priority = issue['priority']['name']

    fields_value = []

    for custom_field in custom_fields:
        if(custom_field['custom_field_id'] == 1 or custom_field['custom_field_id'] == 2 or custom_field['custom_field_id'] == 3 or custom_field['custom_field_id'] == 4):
            fields_value.append(custom_field['value'])    
            

    return summary,description,priority,fields_value

