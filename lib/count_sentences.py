#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self.value = value  # use setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Split using regex to match '.', '!', or '?' followed by space or end of string
        sentence_list = re.split(r'[.!?]+', self.value)
        # Remove empty strings and whitespace-only strings
        sentences = [s.strip() for s in sentence_list if s.strip()]
        return len(sentences)
