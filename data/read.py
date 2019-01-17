import xmltodict


def open_file(file):
    with open(file, 'r') as f:
        s = f.read()
        return s


def parse():
    return xmltodict.parse(open_file('data/dict.xdxf'))['xdxf']['ar']
