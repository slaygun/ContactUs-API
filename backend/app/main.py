from fastapi import FastAPI
from .models import User
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I am working!"}