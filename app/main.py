import os
from fastapi import FastAPI
from dotenv import load_dotenv
from api import router

load_dotenv()

app = FastAPI()
app.include_router(router)