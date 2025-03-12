from app.models.base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

class RelatedArtist(Base):
    __tablename__ = "related_artists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"), nullable=False)
    related_artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"), nullable=False)
