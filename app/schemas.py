from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    genre: str

class BookCreate(BookBase):
    author_id: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    author_id: Optional[int] = None

class Book(BookBase):
    id: int
    author: Author
    rating: float
    
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    text: str
    rating: int

class ReviewCreate(ReviewBase):
    book_id: int

class Review(ReviewBase):
    id: int
    book: Book
    owner: User
    
    class Config:
        orm_mode = True