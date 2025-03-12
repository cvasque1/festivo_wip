from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal


app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Festivo!"}

@app.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    return {"massage": "Database connection successful!"}