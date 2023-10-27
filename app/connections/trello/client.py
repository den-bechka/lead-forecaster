import os
from trello import TrelloClient

client = TrelloClient(
    api_key      = os.getenv('TRELLO_API_KEY'),
    api_secret   = os.getenv('TRELLO_SECRET_KEY'),
    token        = os.getenv('TRELLO_TOKEN'),
    token_secret = os.getenv('TRELLO_SECRET_TOKEN')
)

all_boards = client.list_boards()