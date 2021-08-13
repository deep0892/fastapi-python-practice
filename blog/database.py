from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from slqalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlush=False)

Base = declarative_base()
