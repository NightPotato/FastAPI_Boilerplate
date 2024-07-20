from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DB_URL = os.environ['DB_URL']
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" # Example for PostgresSQL

# TODO: Remove connect_args={"check_same_thread": False} as its only needed for Sqlite Databases.
engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

