import csv
import io
from typing import List, Dict, Tuple

REQUIRED_COLUMNS = ["name", "role", "id"]

def validate_csv(content: str) -> Dict[str, List]:
    """
    Validates CSV content and returns valid rows and invalid rows with reasons.
    """
    valid_rows = []
    invalid_rows = []
    
    # Use io.StringIO to treat string as a file
    f = io.StringIO(content)
    reader = csv.DictReader(f)
    
    # Check if header exists and has required columns
    if not reader.fieldnames:
        return {"error": "CSV file is empty or missing headers"}
    
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
    if missing_cols:
        return {"error": f"Missing required columns: {', '.join(missing_cols)}"}
    
    for row_idx, row in enumerate(reader, start=1):
        errors = []
        # Check for empty fields in required columns
        for col in REQUIRED_COLUMNS:
            if not row.get(col) or not str(row[col]).strip():
                errors.append(f"Field '{col}' is empty")
        
        if errors:
            invalid_rows.append({
                "row": row_idx,
                "data": row,
                "reason": ", ".join(errors)
            })
        else:
            valid_rows.append(row)
            
    return {
        "valid_rows": valid_rows,
        "invalid_rows": invalid_rows
    }
