""" Main code | Proyecto """

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to the FastAPI application!"

