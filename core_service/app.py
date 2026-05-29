from fastapi.templating import Jinja2Templates
from fastapi import Request

from core_service.services.user_service import (
    create_user,
    get_users
)

from core_service.services.collection_service import (
    create_collection,
    get_collections
)

from core_service.services.word_service import (
    add_word,
    get_words,
    delete_word
)

from core_service.services.progress_service import (
    get_all_collections_progress
)

from fastapi.responses import HTMLResponse

import random

import json

from pathlib import Path

from fastapi import FastAPI

from core_service.auth import create_token
from core_service.database.connection import get_connection


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "Vocabulary Trainer API"}


@app.post("/register")
def register(username: str, password: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users(username, password)
        VALUES (%s, %s)
        """,
        (username, password)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return {"message": "User created"}


@app.post("/login")
def login(username: str):
    token = create_token(username)
    return {"access_token": token}


@app.get("/about")
def about():
    file_path = Path(__file__).resolve().parent.parent / "about.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

import os

@app.get("/debug")
def debug():
    return {
        "cwd": os.getcwd(),
        "ok": True
    }



@app.post("/check")
def check(word_id: int, answer: str):
    words = get_words()

    word = None
    for w in words:
        if w[0] == word_id:
            word = w
            break

    if not word:
        return {"error": "word not found"}

    if answer.lower().strip() == word[2].lower().strip():
        return {"result": "correct"}
    else:
        return {
            "result": "wrong",
            "correct": word[2]
        }

@app.get("/ui")
def ui(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/users")
def create_user_api(username: str, password: str):
    create_user(username, password)
    return {"status": "ok"}


@app.get("/collections")
def collections():
    return get_collections()


@app.post("/words")
def add_word_api(original: str, translation: str, example: str, collection_id: int):
    add_word(original, translation, example, collection_id)
    return {"status": "ok"}

@app.get("/train")
def train():
    words = get_words()
    return words

@app.get("/progress")
def progress():
    return get_all_collections_progress()


@app.get("/users")
def users():
    return get_users()


@app.get("/collections")
def collections():
    return get_collections()


@app.get("/words")
def words():
    return get_words()

