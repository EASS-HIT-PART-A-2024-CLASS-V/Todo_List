# Todo List Application

This project is a Todo List application with a FastAPI backend and a Streamlit frontend. The backend handles task management, while the frontend provides a user-friendly interface to interact with the tasks.

## Table of Contents
- [Installation](#installation)
  - [Backend](#backend)
    - [Running the Backend with Docker](#running-the-backend-with-docker)
  - [Frontend](#frontend)
    - [Running the Frontend with Docker](#running-the-frontend-with-docker)
  - [Docker Compose](#docker-compose)
- [API Documentation](#api-documentation)
- [License](#license)

## Installation

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/)

### Clone the Repository
```bash
git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-V/Todo_List.git
cd Todo_List

Backend
Running the Backend with Docker
Build the Docker image:

bash
Copy code
docker build -t todo-backend -f backend.Dockerfile .
Run the Docker container:

bash
Copy code
docker run -p 8000:8000 todo-backend
The backend API will be available at http://localhost:8000.

Frontend
Running the Frontend with Docker
Build the Docker image:

bash
Copy code
docker build -t todo-frontend -f frontend.Dockerfile .
Run the Docker container:

bash
Copy code
docker run -p 8501:8501 todo-frontend
The frontend will be available at http://localhost:8501.

Docker Compose
To run both the backend and frontend together using Docker Compose:

Build and start the services:

bash
Copy code
docker-compose up --build
The backend API will be available at http://localhost:8000 and the frontend will be available at http://localhost:8501.
