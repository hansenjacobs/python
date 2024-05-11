def validate_dict(data, schema, path = ''):
    errors = []
    if not isinstance(schema, dict) or not schema.get('properties'):
        errors.append("schema must be a dict that contains a key named 'properties'")
    
    if not isinstance(data, dict):
        errors.append("data must be a dict")

    errors = validate_property(data, schema['properties'])
    return errors

    
def validate_property(data, schema, path=''):
    errors = []
    for prop, prop_schema in schema.items():
            prop_path = f'{path}.{prop}' if path else prop
            if prop_schema.get('required', False) and prop in data:
                prop_type = prop_schema.get('type', None)
                if prop_type == dict:
                    if isinstance(data[prop], dict):
                        errors.extend(validate_property(data[prop], prop_schema, prop_path))
                    else:
                        errors.append(f'Type mismatch: {prop_path} must be a dict')
                elif prop_type == list:
                    if isinstance(data[prop], list):
                        for i, item in enumerate(data[prop]):
                            index_prop_path = f'{prop_path}[{i}]'
                            errors.extend(validate_property(item, prop_schema['items']['properties'], index_prop_path))
                    else:
                        errors.append(f'Type mismatch: {prop_path} must be a list')
                elif prop_type == str:
                    if isinstance(data[prop], str):
                        if prop_schema.get('length-min') and len(data[prop]) < prop_schema['length-min']:
                            errors.append(f'Minimum length not reached, {prop_path} must be a minimum of {prop_schema['length-min']} chars')
                        if prop_schema.get('length-max') and len(data[prop]) < prop_schema['length-max']:
                            errors.append(f'Maximum length exceeded, {prop_path} must be a maximum of {prop_schema['length-max']} chars')
                    else:
                        errors.append(f'Type mismatch: {prop_path} must be a str')
            else:
                errors.append(f'Missing required property: {prop_path}')
    return errors
            
                      
                 
                 

