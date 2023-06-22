from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# app
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoints
from revapp.endpoints import *
