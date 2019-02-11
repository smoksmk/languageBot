import random
from abc import abstractmethod


class LearnStateBase:
    @abstractmethod
    def check_word(self, answer_word):
        pass


class CheckWordedLearn(LearnStateBase):
    def __init__(self, question_word: str, answers_words: list):
        self.question_word = question_word
        self.answers_words = answers_words

    def check_word(self, answer_word):
        if answer_word in self.answers_words:
            return True
        return False


class CheckLearn:
    def __init__(self, words):
        self.words = self.set_word(words)
        self._generator = self._get_generator_words()
        self.current_word = next(self._generator)

    @staticmethod
    def set_word(words):
        status = []
        for question_word, answers_word in words:
            status.append(CheckWordedLearn(question_word, answers_word))
        return status

    def _get_generator_words(self):
        for next_question in self.words:
            yield next_question

    def check_word(self, answer_word):
        if self.current_word.check_word(answer_word):
            self.current_word = next(self._generator)
            return True
        else:
            return False

    def get_answers_example(self):

        answers_words = [", ".join(i.answers_words) for i in self.words if i.answers_words != self.current_word.answers_words]
        rand_answers = random.sample(answers_words, 3)
        rand_answers.append(", ".join(self.current_word.answers_words))
        random.shuffle(rand_answers)
        return rand_answers

    def __str__(self):
        return self.current_word.question_word

    def __repr__(self):
        return self.current_word.question_word


