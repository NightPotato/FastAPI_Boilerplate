from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


#
# os variable is returning None instead of value. I forget how .env files work in python.
# SQLALCHEMY_DB_URL = os.getenv('DB_URL')
SQLALCHEMY_DB_URL = 'sqlite:///./example.db'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" # Example for PostgresSQL

engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

