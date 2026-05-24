from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI"
    }

@app.get("/endpoint")
def endpoint():
    return {
        "message": "Endpoint from FastAPI"
    }