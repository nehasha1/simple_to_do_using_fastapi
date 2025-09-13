# Simple FastAPI Todo App 

This is a beginner-friendly **FastAPI project**.

## Features
- Add, list, and delete todos
- Swagger UI documentation at `/docs`
- Uses FastAPI + Uvicorn

## Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/simple-fastapi-todo.git
cd simple-fastapi-todo
python3 -m venv venv
source venv/bin/activate   # for Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
