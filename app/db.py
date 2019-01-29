from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

from sqlalchemy.pool import NullPool

from app.config import SQL_ALCHEMY_URI

Base = declarative_base()

engine = create_engine(SQL_ALCHEMY_URI, poolclass=NullPool)

session_maker = sessionmaker(bind=engine)
# Session.configure(bind=engine)


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = session_maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
