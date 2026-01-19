 # Fullstack Docker Assignment (Node.js + Flask)

This project demonstrates a simple fullstack application where:
- **Frontend** is built using **Node.js with Express**
- **Backend** is built using **Flask (Python)**
- Both services communicate with each other using **Docker Compose**
- The entire setup runs in isolated Docker containers

---

## 📁 Project Structure

 fullstack-docker-assignment/
│
├── frontend/
│ ├── app.js
│ ├── package.json
│ ├── Dockerfile
│ └── views/
│ └── index.ejs
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── docker-compose.yml
├── .gitignore
└── README.md


---

## 🚀 Features

- Express-based frontend with HTML form
- Flask backend to process form data
- Inter-service communication using Docker networking
- Separate Dockerfiles for frontend and backend
- Docker Compose for orchestration
- Clean Git repository with ignored unnecessary files

---

## 🖥️ Frontend Details

- Built using **Node.js + Express**
- Uses **EJS** for rendering the form
- Sends form data to Flask backend using **Axios**
- Runs on port **3000**

---

## 🧠 Backend Details

- Built using **Flask**
- Receives form data from frontend
- Processes and returns a response in JSON format
- Runs on port **5000**

---

## 🐳 Docker Configuration

### Frontend Dockerfile
- Uses `node:18-alpine`
- Installs dependencies using `npm install`
- Exposes port `3000`

### Backend Dockerfile
- Uses `python:3.10-slim`
- Installs dependencies from `requirements.txt`
- Exposes port `5000`

### Docker Compose
- Runs both services on the same Docker network
- Frontend communicates with backend using service name `backend`
- Handles service dependencies automatically

---

## ▶️ How to Run the Project

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
docker compose up --build


Access the Application
http://localhost:3000

📦 Docker Hub (Optional)
To push images to Docker Hub:

docker login

docker build -t <dockerhub-username>/node-frontend ./frontend
docker build -t <dockerhub-username>/flask-backend ./backend

docker push <dockerhub-username>/node-frontend
docker push <dockerhub-username>/flask-backend

🚫 Git Ignore
The following files and folders are ignored:

node_modules/
.vscode/
__pycache__/
.env
.DS_Store

📌 Summary

This project demonstrates:

Fullstack application development
Containerization using Docker
Service orchestration using Docker Compose
Clean and production-style folder structure

👤 Author
Ameen Sajid