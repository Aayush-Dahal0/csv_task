from fastapi.responses import JSONResponse
from typing import Any, Optional

def standard_response(success: bool, message: str, data: Optional[Any] = None, status_code: int = 200):
    content = {
        "success": success,
        "message": message
    }
    if data is not None:
        content["data"] = data
    return JSONResponse(content=content, status_code=status_code)
