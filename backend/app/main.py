from fastapi import FastAPI
from models import User
from functions import send_email,text_content
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.environ.get("SMTP_SERVER")
PORT = os.environ.get("PORT")
LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

text = text_content("n@gmail.com", "nabh", "trial2")
send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, TO_EMAIL, text)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "I am working!"}

@app.post("/response", response_model=User)
async def send_details():
    return {"message": "Your details has been sent!"}

