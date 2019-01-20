from sqlalchemy import Column, Table, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from app.db import Base, engine

ru_to_en = Table(
    'ru_to_en', Base.metadata,
    Column('name_ru_id', Integer, ForeignKey('name_ru.id')),
    Column('name_en_id', Integer, ForeignKey('name_en.id'))
)

language_level = Table(
    'language_to_level', Base.metadata,
    Column('language_id', Integer, ForeignKey('language_level.id')),
    Column('name_en_id', Integer, ForeignKey('name_en.id'))
)

learning_word = Table(
    'word_to_user', Base.metadata,
    Column('name_en_id', Integer, ForeignKey('name_en.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)


class NameRu(Base):
    __tablename__ = 'name_ru'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_en = relationship(
        "NameEn",
        secondary=ru_to_en,
        backref=backref(
            'name_ru',
            uselist=True,
        )
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{__class__.name}: {self.name}'


class NameEn(Base):
    __tablename__ = 'name_en'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{__class__.name}: {self.name}'


class Level(Base):
    __tablename__ = 'language_level'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = relationship(
        'NameEn',
        secondary=language_level,
        backref=backref(
            'level'
        )
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{__class__.name}: {self.name}'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level_id = Column(Integer, ForeignKey('language_level.id'))
    level = relationship(
        'Level',
        backref=backref('user')
    )
    words = relationship(
        'NameEn',
        secondary=learning_word,
        backref=backref('words')
    )


if __name__ == "__main__":
    Base.metadata.create_all(engine)
