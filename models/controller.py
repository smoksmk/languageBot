import random

from app.db import session
from models.models import NameEn, NameRu, Level


class Dictionary:
    @staticmethod
    def get_count_word(level=None):
        count = session.query(NameEn)
        if level:
            count.filter(Level.id == level.id)

        return count.count()

    @staticmethod
    def get_level(name):
        return session.query(Level).filter_by(name=name).one()

    def get_random_word(self, level=None):
        count_word = self.get_count_word(level)
        word_id = random.randint(1, count_word)
        word = session.query(NameEn)\
            .filter_by(id=word_id)

        if level:
            word.filter(Level == level)

        result = word.first()
        return result.name, result.name_ru

    @staticmethod
    def get_translate_en_to_ru(word):
        return session.query(NameEn).filter_by(name=word).first()

    @staticmethod
    def get_translate_ru_to_en(word):
        return session.query(NameRu).filter_by(name=word).first()


class Learning:

    def __init__(self, User):
        self._user = User

    def get_word(self, word):
        pass

    def set_answer(self, word):
        pass

