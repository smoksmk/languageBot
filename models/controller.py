import random

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

from app.db import session_scope
from languageBot.models.models import NameEnModel, NameRuModel, LevelModel, UserModel


def get_random_word(session, name=None):
    word = session.query(NameEnModel)
    if name:
        word = word.filter(LevelModel.name == name)\
            .join(NameEnModel.level)

    return word.order_by(func.random()).first()


def save_word_to_user(session, word: NameEnModel, user_id: int):
    user = session.query(UserModel).filter_by(id=user_id).one()
    user.words.append(word)
    session.add(user)
    session.commit()


def get_random_learning_word(session, user_id, limit=10):
    return session.query(NameEnModel)\
        .filter(UserModel.id == user_id)\
        .join(UserModel.words)\
        .order_by(func.random())\
        .limit(limit).all()


def get_translate_en_to_ru(session, word):
    return session.query(NameEnModel).filter_by(name=word).first()


def get_translate_ru_to_en(session, word):
    return session.query(NameRuModel).filter_by(name=word).first()


def save_user(session, data, source_system, level):
    user = UserModel()
    user.name = data.id
    user.source_system_id = source_system
    user.level = level
    user.fullname = f'{data.first_name} {data.last_name}'
    session.add(user)
    session.commit()
    return user


def get_user_id(session, data, source_system):
    try:
        return session.query(UserModel).filter_by(name=data.id, source_system_id=source_system).one().id
    except NoResultFound:
        level = session.query(LevelModel).filter_by(name='elementary').one().id
        return save_user(session, data, source_system, level)


def get_user_by_id(session, user_id):
    return session.query(UserModel).filter_by(id=user_id).one()


if __name__ == '__main__':
    with session_scope() as session:
        print(get_random_learning_word(session, 2))

