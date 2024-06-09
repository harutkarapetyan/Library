from sqlalchemy import Column, Integer, String, text, ForeignKey, Float, ARRAY, Boolean, Date
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime

from database import Base


class UserSetting(Base):
    __tablename__ = "user_settings"

    setting_id = Column(Integer, nullable=False, primary_key=True)
    language = Column(String, nullable=False, server_default="en")
    background_color = Column(String, nullable=False, server_default="white")
    font_size = Column(Float, nullable=False, server_default="12.0")

    user_id = Column(Integer, nullable=False)


class PossibleSetting(Base):
    __tablename__ = "possible_settings"

    id = Column(Integer, nullable=False, primary_key=True)
    possible_languages = Column(ARRAY(String), nullable=False)
    possible_background_colors = Column(ARRAY(String), nullable=False)
    possible_settings_font_size = Column(Float, nullable=False)


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    passport_seria = Column(Integer, nullable=False, unique=True)
    status = Column(Boolean, nullable=False, server_default="False")


class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    publisher_id = Column(Integer, ForeignKey('publisher.publisher_id'))
    author_id = Column(Integer, ForeignKey('authors.author_id'))


class Purchases(Base):
    __tablename__ = "purchases"

    purchases_id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False, server_default=text("now()"))
    end_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))


class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    born_date = Column(Date, nullable=False)


class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phon_number = Column(String, nullable=False)







