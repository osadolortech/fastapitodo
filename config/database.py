from os import getenv
from pymongo import MongoClient

URL = getenv("URL")

client = MongoClient(URL)

db = client.todo_application

collections_todo = db["todo_api"]