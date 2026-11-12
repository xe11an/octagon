from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    # добавил unique чтобы не было повторов
    title = Column(String, unique=True, index=True, nullable=False)

    books = relationship("Book", back_populates="category", cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    # unique
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    
    price = Column(Numeric(10, 2), nullable=False)
    
    url = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    
    category = relationship("Category", back_populates="books")