import json

def parse_input(input: str):
    data = json.loads(input)
    return (data["group_type"], data["dt_from"], data["dt_upto"])

