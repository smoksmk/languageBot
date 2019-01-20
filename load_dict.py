from app.db import session
from models.models import NameEn, NameRu, Level
from data.read import parse_en_to_ru, load_elementary


def translate_ru(word):
    res = session.query(NameRu).filter_by(name=word).all()
    for word in res:
        for word2 in word.name_en:
            print(word.name, word2.name)


def translate_en(word):
    res = session.query(NameEn).filter_by(name=word).all()
    for word in res:
        for word2 in word.name_ru:
            print(word.name, word2.name)


level = session.query(Level).filter_by(name='elementary').one()

for name_en, name_ru in load_elementary():
    en = session.query(NameEn).filter_by(name=name_en.lower()).first()
    if en:
        en.level.append(level)
        session.add(en)
    else:
        print("Добовляем новое слово")
        word_en = NameEn(name=name_en)
        word_ru = NameRu(name=name_ru)
        word_en.level.append(level)
        word_en.name_ru.append(word_ru)
        session.add(word_en)
        session.add(word_ru)

    session.commit()
    # print(en, name_en, name_ru)
    # print(i)

# translate_ru('отправлять')
# translate_en('send')

# for name_en, name_ru in parse_en_to_ru():
#     # print(name_en, name_ru)
#     en = session.query(NameEn, NameRu).filter(~NameEn.name == name_en, ~NameRu.name == name_ru).first()
#     if en:
#         print(en)

    # if en:
#         # print('есть английское слово')
#         ru = session.query(NameRu).filter_by(name=name_ru).first()
#         if not ru:
#             print('нет перевода сохраняем')
#             ru = NameRu(name=name_ru)
#             ru.name_.append(ru)
#             session.add(ru)
#             session.add(en)
#
#     else:
#         print('нет такого английского слова сохраняем')
#         ru = session.query(NameRu).filter_by(name_ru).first()
#         if not ru:
#             print('нет такого русского слова сохраняем')
#             ru = NameRu()
#         en = NameEn(name=name_en)
#         print('сохраняем связь')
#         en.name_ru.append(ru)
#         session.add(ru)
#         session.add(en)
#
#     session.commit()
