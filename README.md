<!DOCTYPE html>
<html>
<head>
    
</head>
<body>

<h1>Todo List Application</h1>
<p>This project is a Todo List application with a FastAPI backend and a Streamlit frontend. The backend handles task management, while the frontend provides a user-friendly interface to interact with the tasks.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#backend">Backend</a></li>
    <li><a href="#frontend">Frontend</a></li>
    <li><a href="#docker-compose">Docker Compose</a></li>
    <li><a href="#api-documentation">API Documentation</a></li>
</ul>

<h2 id="installation">Installation</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Docker</li>
    <li>Git</li>
</ul>

<h3>Clone the Repository</h3>
<pre><code>git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-V/Todo_List.git
cd Todo_List</code></pre>

<h2 id="backend">Backend</h2>

<h3>Running the Backend with Docker</h3>
<p>Build the Docker image:</p>
<pre><code>docker build -t todo-backend -f backend.Dockerfile .
</code></pre>
<p>Run the Docker container:</p>
<pre><code>docker run -p 8000:8000 todo-backend
</code></pre>
<p>The backend API will be available at <a href="http://localhost:8000">http://localhost:8000</a>.</p>

<h2 id="frontend">Frontend</h2>

<h3>Running the Frontend with Docker</h3>
<p>Build the Docker image:</p>
<pre><code>docker build -t todo-frontend -f frontend.Dockerfile .
</code></pre>
<p>Run the Docker container:</p>
<pre><code>docker run -p 8501:8501 todo-frontend
</code></pre>
<p>The frontend will be available at <a href="http://localhost:8501">http://localhost:8501</a>.</p>

<h2 id="docker-compose">Docker Compose</h2>

<p>To run both the backend and frontend together using Docker Compose:</p>
<p>Build and start the services:</p>
<pre><code>docker-compose up --build
</code></pre>
<p>The backend API will be available at <a href="http://localhost:8000">http://localhost:8000</a> and the frontend will be available at <a href="http://localhost:8501">http://localhost:8501</a>.</p>

<h2 id="api-documentation">API Documentation</h2>

<p>The API documentation is automatically generated and available at <a href="http://localhost:8000/docs">http://localhost:8000/docs</a> when the backend server is running.</p>

</body>
</html>
