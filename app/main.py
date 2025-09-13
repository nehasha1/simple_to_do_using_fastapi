from fastapi import FastAPI

app = FastAPI()

# In-memory storage (like a database, but simple)
todos = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Simple Todo API!"}

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.post("/todos/{item}")
def add_todo(item: str):
    todos.append(item)
    return {"message": f"Todo '{item}' added!", "todos": todos}

@app.delete("/todos/{item}")
def delete_todo(item: str):
    if item in todos:
        todos.remove(item)
        return {"message": f"Todo '{item}' deleted!", "todos": todos}
    return {"error": "Todo not found!"}
