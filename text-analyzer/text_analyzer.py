import re
from collections import Counter
from functools import cached_property
from typing import Iterator, List, Dict
from datetime import datetime


class TextAnalyzer:
    def __init__(self, file_name: str) -> None:
        with open(file_name, 'r') as file:
            self.text = file.read()
            self.sentences = re.findall(r'\b[^.!?]+[.!?]+', self.text)
            self.words = [str(word).lower() for word in re.findall(r'\w+', self.text)]

    @cached_property
    def characters_frequency(self) -> Dict[str, int]:
        frequency = Counter(self.text)
        return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    @property
    def characters_frequency_as_percentage_of_total(self) -> Dict[str, int]:
        return {
            char: f'{frequency / len(self.text) * 100:.2f}%'
            for char, frequency in self.characters_frequency.items()
        }

    @property
    def average_word_length(self) -> float:
        return round(sum(len(word) for word in self.words) / len(self.words), 2)

    @property
    def average_number_of_words_in_sentence(self) -> float:
        return round(len(self.words) / len(self.sentences), 2)

    @property
    def top_10_most_used_words(self) -> Iterator[str]:
        most_common = Counter(self.words).most_common(10)
        most_common = (word_data[0] for word_data in most_common)

        return most_common

    @cached_property
    def palindrome_words(self) -> List[str]:
        return [word for word in self.words if self.is_palindrome(word)]

    @property
    def text_without_spaces_and_punctuation(self) -> str:
        return re.sub(r'\W', '', self.text)

    @property
    def reversed_text_with_saved_words(self) -> str:
        return ' '.join(self.text.split()[::-1])

    @staticmethod
    def top_10_longest(objects: List[str]) -> List[str]:
        return sorted(set(objects), key=len, reverse=True)[:10]

    @staticmethod
    def top_10_shortest(objects: List[str]) -> List[str]:
        return sorted(set(objects), key=len)[:10]

    @staticmethod
    def is_palindrome(string: str) -> bool:
        return string == string[::-1]

    @staticmethod
    def generated_datetime() -> str:
        return datetime.now().strftime("%Y.%m.%d %H:%M:%S")
