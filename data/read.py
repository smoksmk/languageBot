import xmltodict
import re


def open_file(file):
    with open(file, 'r') as f:
        s = f.read()
        return s


def parse_ru_to_en():
    data = xmltodict.parse(open_file('data/dict.xdxf'))['xdxf']['ar']
    pattern = re.compile(r'[^a-zA-Z]')
    return [(i['k'], pattern.sub('', i['#text']).lower()) for i in data]


def parse_en_to_ru():
    data = xmltodict.parse(open_file('data/dict_en_to_ru.xdxf'))['xdxf']['ar']
    pattern = re.compile(r'[^а-яА-ЯёЁ]')
    return [(i['k'], pattern.sub('', i['#text']).lower()) for i in data]


def load_elementary():
    data = open_file('data/elementaru.txt')
    result = []
    for i in data.splitlines():
        word = i.split(' ')
        # print(word)
        result.append((word[0], word[3]))
    return result
