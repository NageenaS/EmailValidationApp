# EmailValidationApp

This Email Validation App is a simple web-based tool built with Flask that allows users to validate email addresses. It uses the AbstractAPI email validation service to check the validity of an email and returns various attributes such as deliverability, format validity, and other parameters.

## Features

- Validates the format, quality, and deliverability of an email address.
- Detects if the email is from a free provider, a disposable service, or if it is role-based.
- Provides an auto-correction suggestion for common typos in email addresses.

## Prerequisites

- **Python 3.x
- **AbstractAPI API Key**: Sign up on [AbstractAPI](https://www.abstractapi.com/) and get your API key for the Email Validation API.

## Setup

1. **Clone the repository**:
   ```
   git clone https://github.com/<your-username>/Email-Validation-App.git
   cd Email-Validation-App
   ```
2. **Install required dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Deploy with Docker**:
You can quickly deploy the application using Docker. Follow these steps:
Pull the pre-built image:
```
docker pull nageenashaik/emailvalidation
```
- Start the container:
```
docker run -d --name email-validation nageenashaik/email-validation
```
- If you're running it in a Docker container:
```
  docker exec -it  email-validation python app.py
```
4. **Run the Flask App:**
   ```
   python app.py
   ```
5. **Access the App**:
   Open your web browser and go to `http://127.0.0.1:5000` to access the application.


## Usage

After launching the application, you can utilize the interface to:

- Enter an email address in the provided form on the home page.
- Submit the email for validation.
- View detailed results on the validity and status of the email, including attributes like deliverability, format validity, and whether it’s from a disposable or free email provider.
  ![Screenshot 2024-11-05 135926](https://github.com/user-attachments/assets/c587e903-d26c-4cf1-a18f-9ea94406999b)
  ![Screenshot 2024-11-05 140006](https://github.com/user-attachments/assets/9dec310d-f2fb-4212-9b31-bda83ce481d7)


## Docker Hub
Docker Hub is a cloud-based repository that allows users to store, share, and manage Docker images. The StockApp is also available on Docker Hub. 
You can find the image [here](https://hub.docker.com/r/nageenashaik/emailvalidation) (replace with your actual Docker Hub link). This allows you to easily deploy the application without building the image locally.
