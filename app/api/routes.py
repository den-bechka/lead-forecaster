from fastapi import APIRouter
from models import model
from connections import TrelloClient
from fastapi.responses import JSONResponse
from trello import Board

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/predict/{data}")
def predict(data: str):
    prediction = model.predict(data)
    return {"prediction": prediction}


@router.get("/trello/boards")
def trello_boards():
    boards = TrelloClient.list_boards()
    return boards[0].name
