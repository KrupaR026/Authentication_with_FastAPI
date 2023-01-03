from server.database.database import base
from sqlalchemy import Column, String, DateTime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime


def date_time():
    return datetime.utcnow()


class User(base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=date_time)
    updated_at = Column(DateTime, default=date_time)
