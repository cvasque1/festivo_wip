from fastapi import FastAPI, Depends
from app.routes import health, auth


app = FastAPI()

# Include Auth Routes
app.include_router(health.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Festivo!"}