from app.models.base import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Festival(Base):
    __tablename__ = "festivals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    last_updated = Column(TIMESTAMP, server_default="now()")