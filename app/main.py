import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add")
async def add_item(item: str) -> dict:
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client.test
    collection = db.test
    collection.insert_one({"item": item})
    return {"message": "Item added successfully"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
