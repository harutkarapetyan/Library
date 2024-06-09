from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/library"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
