# PortfolioMailer-Backend

**PortfolioMailer-Backend** is a FastAPI-based backend service designed to handle contact form submissions from a portfolio website. This backend accepts user input (name, email, and message) via a POST request, sends an email notification to a specified recipient, and responds to the client asynchronously. This service is containerized with Docker for easy deployment.

## Features

- **FastAPI REST API**: A fast and modern API with automatic documentation.
- **Asynchronous Email Sending**: Uses threading to handle email sending in the background.
- **Environment-Based Configuration**: Manages sensitive credentials with environment variables.
- **Dockerized Setup**: Easily deployable with Docker and Docker Compose.
- **Cross-Origin Resource Sharing (CORS)**: Configured for secure interaction with frontends.

## Requirements

- **Python 3.7+**
- **Docker & Docker Compose**

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/portfoliomailer-backend.git
cd portfoliomailer-backend
```
### 2. Create a .env File
Create a .env file in the root directory with your SMTP configuration for sending emails.
``` bash
SMTP_SERVER=smtp.gmail.comSMTP_SERVER: SMTP server (e.g., smtp.gmail.com for Gmail).
SMTP_PORT: SMTP port (587 for TLS, 465 for SSL).
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password  # If using Gmail with 2FA, generate an app password
FROM_EMAIL=your_email@gmail.com
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=xxxx xxxx xxxx
```
- SMTP_SERVER: SMTP server address (e.g., smtp.gmail.com for Gmail).
- SMTP_PORT: SMTP port (587 for TLS, 465 for SSL).
- SMTP_USERNAME and SMTP_PASSWORD: Your email and password (use an app password if using Gmail  with two-factor authentication).
- FROM_EMAIL: Email address to appear as the sender.
- TO_EMAIL: Recipient email address.

### 3. Build and Run with Docker Compose
Build and run the application using Docker Compose:

```bash
docker-compose up -d
```
This will start the backend service on http://localhost:8000.

### 4. Test the Endpoint
You can test the API by sending a POST request to http://localhost:8000/send-email with the following JSON body:
```bash
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "message": "Hello, this is a test message."
}
```
Example response:
```bash
{
  "message": "Email is being sent in the background"
}
```

## Project Structure

```bash
portfoliomailer-backend/
├── main.py               # Main FastAPI application
├── .env                  # Environment variables file (not included in version control)
├── Dockerfile            # Docker configuration for building the image
├── docker-compose.yml    # Docker Compose file for orchestrating containers
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```


