from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///models/database.sqlite')

db = sessionmaker()
db.configure(bind=engine)
session = db()
