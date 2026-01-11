# Backend Intern Task - CSV Processor

This is my implementation of the CSV upload and validation backend task. It handles file uploads, validates data against specific rules, and logs everything for easy debugging.

## Core Features
- **CSV Upload**: Only accepts `.csv` files.
- **Validation**: 
  - Required columns: `name`, `role`, `id`.
  - Ensures no empty values in these columns.
  - Returns a report of valid and invalid rows.
- **Logging**: All events (success, validation errors, server crashes) are logged with a timestamp in `YYYY-MM-DD HH:MM:SS | TYPE | MESSAGE` format.
- **APIs**:
  - `POST /upload-csv`: Processes the file.
  - `GET /records`: Returns all valid processed records.

## Setup
1. **Environment**: `python -m venv venv` and activate it.
2. **Install**: `pip install -r requirements.txt`
3. **Run**: `uvicorn app.main:app --reload` (Server runs at `http://127.0.0.1:8000`)

## Testing
- **Postman**: I've created a shared collection for testing: [Postman Link](https://aayushdahal-4740576.postman.co/workspace/Postman-tutorial~141fb3db-da77-4c52-a993-b8fc8247022d/collection/45506213-1b7ebfa9-fd40-42f8-a4bd-3d1069617b7b?action=share&creator=45506213)
- Use **form-data** with the key `file` set to a physical `.csv` file.

