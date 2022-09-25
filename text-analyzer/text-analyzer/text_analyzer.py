import re
import math
from time import time
from datetime import datetime
from collections import Counter
from functools import cached_property
from typing import Iterator, List, Dict


class TextAnalyzer:
    def __init__(self, text: str) -> None:
        self.text = text
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
        return datetime.now().strftime('%Y.%m.%d %H:%M:%S')

    def __str__(self) -> str:
        t1 = time()

        result = [
            "Statistical information:",
            f"Number of characters: {len(self.text)}",
            f"Number of words: {len(self.words)}",
            f"Number of sentences: {len(self.sentences)}",
            f"Frequency of characters: {self.characters_frequency}",
            f"Distribution of characters as a percentage of total: {self.characters_frequency_as_percentage_of_total}",
            f"Average word length: {self.average_word_length}",
            f"The average number of words in a sentence: {self.average_number_of_words_in_sentence}",
            f"Top 10 most used words: {', '.join(self.top_10_most_used_words)}",
            f"Top 10 longest words: {', '.join(TextAnalyzer.top_10_longest(self.words))}",
            f"Top 10 shortest words: {', '.join(TextAnalyzer.top_10_shortest(self.words))}",
            "\nTop 10 longest sentences:\n",
            *TextAnalyzer.top_10_longest(self.sentences),
            "\nTop 10 shortest sentences:\n",
            *TextAnalyzer.top_10_shortest(self.sentences),
            f"\nNumber of palindrome words: {len(self.palindrome_words)}",
            f"Top 10 longest palindrome words: {', '.join(TextAnalyzer.top_10_longest(self.palindrome_words))}",
            f"Top 10 shortest palindrome words: {', '.join(TextAnalyzer.top_10_shortest(self.palindrome_words))}",
            f"Is the whole text a palindrome? (without whitespaces and punctuation marks): {'Yes' if TextAnalyzer.is_palindrome(self.text_without_spaces_and_punctuation) else 'No'}"
            f"\nThe reversed text:\n {self.text[::-1]}",
            f"\nThe reversed text but the character order in words kept intact:\n {self.reversed_text_with_saved_words}",
        ]

        t2 = time()
        result.append(f'\nAnalyzed in {math.ceil((t2 - t1) * 1000)}ms\n\n')

        return '\n'.join(result)
