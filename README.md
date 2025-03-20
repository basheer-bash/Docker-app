# Flask Docker Application

This is a simple Flask app running in Docker with a MySQL database. It demonstrates the basics of setting up a containerized Python web application.

## Features
- **Routes**:
  - `/` - Fetches a message from MySQL and displays a counter.
  - `/showcounter` - Displays the current counter value.
- **Database**: MySQL with Docker volume for persistent storage.
- **Environment**: Configurable with `.env`.

## Requirements
- Docker & Docker Compose installed on your system.

## Create a .env file with:
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=mydb
MYSQL_USER=myuser
MYSQL_PASSWORD=mypassword

## Build and start the containers:
docker-compose up --build

## Access the app: 
http://localhost:5000 -
http://localhost:5000/showcounter

## Project Structure
flask-docker/
├── app/
│   └── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env

