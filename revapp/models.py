from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime


class Model(DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[datetime]      = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime]      = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at: Mapped[datetime]      = mapped_column(DateTime, default=datetime.utcnow)

class Review(Model):
    __tablename__ = 'reviews'

    id: Mapped[int]              = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int]         = mapped_column(Integer)
    reviewer_id: Mapped[int]     = mapped_column(Integer)
    rating: Mapped[int]          = mapped_column(Integer)
    review: Mapped[str]          = mapped_column(String(2048))
