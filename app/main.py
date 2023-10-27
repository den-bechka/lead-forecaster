from fastapi import FastAPI
from api import router

print('test')

app = FastAPI()

app.include_router(router)
