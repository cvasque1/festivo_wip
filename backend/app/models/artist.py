from app.models.base import Base
from sqlalchemy import Column, String, Integer, ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Artist(Base):
    __tablename__ = "artists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    spotify_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    genres = Column(ARRAY(String), nullable=False)
    popularity = Column(Integer, nullable=False)
    image_url = Column(String, nullable=True)
    spotify_url = Column(String, nullable=True)
    last_updated = Column(TIMESTAMP, server_default="now()")