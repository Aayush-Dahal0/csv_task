from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.records import router as records_router

app=FastAPI(title="CSV upload backend")

app.include_router(upload_router)
app.include_router(records_router)
