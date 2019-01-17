from sqlalchemy import Column, Table, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from app.db import Base

association_table = Table(
    'ru_to_en', Base.metadata,
    Column('name_ru_id', Integer, ForeignKey('name_ru.id')),
    Column('name_en_id', Integer, ForeignKey('name_en.id'))
)


class NameRu(Base):
    __tablename__ = 'name_ru'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship(
        "Child",
        secondary=association_table,
        backref=backref(
            'employees',
            uselist=True,
        )
    )


class NameEn(Base):
    __tablename__ = 'name_en'
    id = Column(Integer, primary_key=True)
    name = Column(String)
