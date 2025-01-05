# Python Backend Counter App

This is a simple Python backend built using Flask and SQLite to handle a counter app.

## Features

- GET `/counter`: Fetch the current counter value.
- POST `/increment`: Increment the counter and return the updated value.

## Requirements

- Python 3.x
- Flask
- Flask-CORS

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   ```

2. Install dependencies:

pip install -r requirements.txt

3.Run the backend:

python server.py

Other note:

Backend is accessible on http://0.0.0.0:3000 or http://127.0.0.1:3000.

How to Test

Get Counter: Open your browser or a tool like Postman, and make a GET request to:
arduino
Copy code
http://127.0.0.1:3000/counter
Increment Counter: Make a POST request to:
arduino
Copy code
http://127.0.0.1:3000/increment

This is a development server and should not be used in production without a proper WSGI server.
CORS is enabled for testing with web frontends.