from typing import List, Dict

# In-memory storage for valid records
valid_records: List[Dict] = []

def add_records(records: List[Dict]):
    global valid_records
    valid_records.extend(records)

def get_all_records():
    return valid_records
