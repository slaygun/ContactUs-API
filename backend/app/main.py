from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import User
from .functions import send_email, text_content
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

SMTP_SERVER = os.environ.get("SMTP_SERVER")
PORT = os.environ.get("PORT")
LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

app = FastAPI()

# Define the origins that should be allowed to make requests to your FastAPI app
origins = [
    "http://localhost:5173",
    # Add other origins if needed
]

# Add the CORSMiddleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "I am working!"}

@app.post("/response", response_model=User)
async def send_details(data: User):
    try:
        text = text_content(data.email, data.fname, data.lname, data.message)
        send_email(SMTP_SERVER, PORT, LOGIN, PASSWORD, TO_EMAIL, text)
    except smtplib.SMTPException as e:
        raise HTTPException(status_code=500, detail="Failed to send email: " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred: " + str(e))
    
    return data
