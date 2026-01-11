from fastapi import APIRouter, UploadFile, File
from app.services.csv_validator import validate_csv
from app.services.store import add_records
from app.utils.responses import standard_response
from app.utils.logger import logger

router = APIRouter()

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    # 1. Reject other file types
    if not file.filename.endswith('.csv'):
        logger.error(f"Failed upload attempt: file {file.filename} is not a CSV")
        return standard_response(
            success=False, 
            message="Only .csv files are allowed", 
            status_code=400
        )
    
    try:
        # 2. Read CSV and convert it to JSON
        content = await file.read()
        decoded_content = content.decode("utf-8")
        
        # 3. CSV Validation
        validation_result = validate_csv(decoded_content)
        
        if "error" in validation_result:
            logger.error(f"CSV Header Validation Error: {validation_result['error']}")
            return standard_response(
                success=False, 
                message=validation_result["error"], 
                status_code=400
            )
        
        valid_rows = validation_result["valid_rows"]
        invalid_rows = validation_result["invalid_rows"]
        
        # 4. Storage & Logging
        if valid_rows:
            add_records(valid_rows)
            logger.info(f"Successfully uploaded {len(valid_rows)} records from {file.filename}")
        
        if invalid_rows:
            logger.warning(f"Validation errors in {file.filename}: {len(invalid_rows)} rows rejected")
        
        return standard_response(
            success=True,
            message="CSV processed successfully",
            data={
                "valid_rows": valid_rows,
                "invalid_rows": invalid_rows
            }
        )
        
    except Exception as e:
        logger.error(f"Server Error during CSV upload: {str(e)}")
        return standard_response(
            success=False,
            message="An internal server error occurred",
            status_code=500
        )
