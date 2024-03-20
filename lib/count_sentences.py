import io
import sys

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.') if self._value else False

    def is_question(self):
        return self.value.endswith('?') if self.value else False

    def is_exclamation(self):
        return self.value.endswith('!') if self.value else False

    def count_sentences(self):
        if not self._value:
            return 0
        count = 0
        in_sentence = False
        for char in self._value:
            if char in ['.', '?', '!']:
                if not in_sentence:
                    count += 1
                    in_sentence = True
            else:
                in_sentence = False
        return count
