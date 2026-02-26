from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ping, todo_api
from app.db import init_db
import logging

log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI(title="FASTApi Todo")

    application.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    
    application.include_router(ping.router, tags=["health"])
    application.include_router(todo_api.router, prefix="/todos", tags=["Todos"])

    init_db(application)

    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")