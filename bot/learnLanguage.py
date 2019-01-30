import random
from abc import abstractmethod


class LearnStateBase:
    @abstractmethod
    def check_word(self, word):
        pass


class WordLearn(LearnStateBase):
    def __init__(self, word_en: str, word_ru: list):
        self.word_ru = word_ru
        self.word_en = word_en

    def check_word(self, word):
        if word in self.word_ru:
            return True
        return False


class Learn:
    def __init__(self, words):
        self.words = self.set_word(words)
        self.current_word = self.words[0]

    @staticmethod
    def set_word(words):
        status = []
        for data in words:
            status.append(WordLearn(data['word_en'], data['words_ru']))
        return status

    def next_word(self):
        if not self.current_word:
            self.current_word = self.words[0]
        else:
            index = self.words.index(self.current_word)
            if index < len(self.words) - 1:
                index += 1
            else:
                raise StopIteration

            self.current_word = self.words[index]
        return self.current_word

    def check_word(self, word_ru):
        if self.current_word.check_word(word_ru):
            self.next_word()
            return True
        else:
            return False

    def get_answers_example(self):

        answers = [", ".join(i.word_ru) for i in self.words if i.word_ru != self.current_word.word_ru]
        rand_answers = random.sample(answers, 3)
        rand_answers.append(", ".join(self.current_word.word_ru))
        random.shuffle(rand_answers)
        return rand_answers

    def __str__(self):
        return self.current_word.word_en

    def __repr__(self):
        return self.current_word.word_en


test_word = [
    {'word_en': 'and', 'words_ru': ['и']},
    {'word_en': 'or', 'words_ru': ['или']},
    {'word_en': 'word', 'words_ru': ['слово']},
    {'word_en': 'current', 'words_ru': ['текущий']},
    {'word_en': 'simple', 'words_ru': ['образец', 'пробовать']},

]

if __name__ == '__main__':
    word = Learn(test_word)
    print(word)
    answers = word.get_answers_example()
    print(answers)
