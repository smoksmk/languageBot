from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///orm_in_detail.sqlite')

db = sessionmaker()
db.configure(bind=engine)
session = db()
