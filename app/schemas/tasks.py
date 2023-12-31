from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(UUID(as_uuid=True), primary_key=True)
    statement = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
