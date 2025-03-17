from fastapi import FastAPI
from app.routes import user

app = FastAPI(title="FastAPI Project", description="A structured FastAPI application")

# Include routes
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "FastAPI project is running!"}
