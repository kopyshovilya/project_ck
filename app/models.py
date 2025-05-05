from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    reviews = relationship("Review", back_populates="owner")

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    genre = Column(String)
    rating = Column(Float, default=0.0)
    
    author = relationship("Author", back_populates="books")
    reviews = relationship("Review", back_populates="book")

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    books = relationship("Book", back_populates="author")

class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    book = relationship("Book", back_populates="reviews")
    owner = relationship("User", back_populates="reviews")