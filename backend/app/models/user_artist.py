from app.models.base import Base
from sqlalchemy import Column, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum


class TimeframeEnum(enum.Enum):
    LAST_MONTH = "last_month"
    LAST_6_MONTHS = "last_6_months"
    ALL_TIME = "all_time"


class UserArtist(Base):
    __tablename__ = "user_artists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"), nullable=False)
    timeframe = Column(Enum(TimeframeEnum, name="timeframe_enum"), nullable=False)
    retrieved_at = Column(TIMESTAMP, server_default="now()")