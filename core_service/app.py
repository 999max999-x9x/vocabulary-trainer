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

@app.get("/ui", response_class=HTMLResponse)
def ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vocabulary Trainer</title>

        <style>

            body{
                margin:0;
                font-family:Arial;
                background:#0f0f0f;
                color:white;
            }

            .container{
                padding:40px;
            }

            h1{
                font-size:48px;
            }

            button{
                padding:12px 20px;
                margin:10px;
                border:none;
                border-radius:10px;
                cursor:pointer;
                font-size:16px;
            }

            .card{
                background:#1c1c1c;
                padding:20px;
                border-radius:16px;
                margin-top:20px;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>Vocabulary Trainer</h1>

            <button onclick="loadUsers()">Users</button>

            <button onclick="loadCollections()">
                Collections
            </button>

            <button onclick="loadWords()">
                Words
            </button>

            <button onclick="loadTraining()">
                Training
            </button>

            <button onclick="loadProgress()">
                Progress
            </button>

            <div id="output" class="card">

                Data will appear here

            </div>

        </div>

        <script>

            async function loadUsers(){

                let res = await fetch("/users")

                let data = await res.json()

                document.getElementById("output").innerHTML =
                    JSON.stringify(data,null,2)

            }

            async function loadCollections(){

                let res = await fetch("/collections")

                let data = await res.json()

                document.getElementById("output").innerHTML =
                    JSON.stringify(data,null,2)

            }

            async function loadWords(){

                let res = await fetch("/words")

                let data = await res.json()

                document.getElementById("output").innerHTML =
                    JSON.stringify(data,null,2)

            }

            async function loadTraining(){

                let res = await fetch("/train")

                let data = await res.json()

                document.getElementById("output").innerHTML =
                    JSON.stringify(data,null,2)

            }

            async function loadProgress(){

                let res = await fetch("/progress")

                let data = await res.json()

                document.getElementById("output").innerHTML =
                    JSON.stringify(data,null,2)

            }

        </script>

    </body>
    </html>
    """

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

