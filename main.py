# main.py
import threading
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv(dotenv_path="conf.env")

app = FastAPI(
    docs_url=None,
    openapi_url=None,
    swagger_ui_oauth2_redirect_url=None,
    redoc_url=None,
)

orgins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define the request body model
class EmailRequest(BaseModel):
    name: str
    email: EmailStr
    message: str
    to_email: EmailStr

# Email configuration using environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Default to smtp.gmail.com
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default to 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")
# Ensure that required values are not empty
if not SMTP_SERVER or not SMTP_USERNAME or not SMTP_PASSWORD:
    raise ValueError("SMTP configuration is incomplete.")
# Print to verify
print("SMTP_SERVER:", SMTP_SERVER)
print("SMTP_PORT:", SMTP_PORT)
print("SMTP_USERNAME:", SMTP_USERNAME)
print("SMTP_PASSWORD:", SMTP_PASSWORD)
print("FROM_EMAIL:", FROM_EMAIL)


def send_email_background(email_data):
    """Function to send email in a background thread."""
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg["From"] = FROM_EMAIL
        msg["To"] = email_data["to_email"]
        msg["Subject"] = "New Message from Your Portfolio"
        
        body = f"Name: {email_data['name']}\nEmail: {email_data['email']}\nMessage: {email_data['message']}"
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, email_data["to_email"], msg.as_string())
    except Exception as e:
        print("Failed to send email in background:", e)

@app.post("/send-email")
async def send_email(request: EmailRequest):
    email_data = request.dict()
    # Start the background email sending process
    threading.Thread(target=send_email_background, args=(email_data,)).start()
    # Immediately return a success message to the user
    return {"message": "Email is being sent in the background"}


for r in app.routes:
    print(r.path)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)