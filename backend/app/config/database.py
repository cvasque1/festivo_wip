# Necessary modules neede to make the code work
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Load database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine. parameter specifies database conection details
engine = create_engine(DATABASE_URL)

# Create a session factor. Configured the session to be used for db operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency fctn to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
