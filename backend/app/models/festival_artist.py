from app.models.base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

class FestivalArtist(Base):
    __tablename__ = "festival_artists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    festival_id = Column(UUID(as_uuid=True), ForeignKey("festivals.id"), nullable=False)
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"), nullable=False)
