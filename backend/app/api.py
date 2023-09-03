from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# GET ROUTE
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello, World!"}

todos = [
    {
        "id": "1",
        "item": "Read Stephen King's Cujo"
    },
    {
        "id": "2",
        "item": "Go for shopping"
    },
    {
        "id": "3",
        "item": "Cook dinner"
    }
]

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return { "data": todos }

# POST ROUTE
@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": { "Todo added." }
    }

# PUT ROUTE
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }
    
# DELETE ROUTE
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }