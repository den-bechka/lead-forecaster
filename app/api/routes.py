from fastapi import APIRouter
from models import model

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/predict/{data}")
def predict(data: str):
    prediction = model.predict(data)
    return {"prediction": prediction}