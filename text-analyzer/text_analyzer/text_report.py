from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TextReport:
    number_of_characters: int
    number_of_words: int
    number_of_sentences: int
    frequency_of_characters: Dict[str, float]
    distribution_of_characters: Dict[str, str]
    average_word_length: float
    average_words_in_sentence: float
    ten_most_used_words: List[str]
    ten_longest_words: List[str]
    ten_shortest_words: List[str]
    ten_longest_sentences: List[str]
    ten_shortest_sentences: List[str]
    number_of_palindrome_words: int
    ten_longest_palindrome_words: List[str]
    ten_shortest_palindrome_words: List[str]
    is_text_a_palindrome: bool
    reversed_text: str
    reversed_text_with_saved_words: str
    analyzing_time: int = -1

    def __str__(self):
        result = [
            "Statistical information:",
            f"Number of characters: {self.number_of_characters}",
            f"Number of words: {self.number_of_words}",
            f"Number of sentences: {self.number_of_sentences}",
            f"Frequency of characters: {self.frequency_of_characters}",
            f"Distribution of characters as a percentage of total: {self.distribution_of_characters}",
            f"Average word length: {self.average_word_length}",
            f"The average number of words in a sentence: {self.average_words_in_sentence}",
            f"Top 10 most used words: {', '.join(self.ten_most_used_words)}",
            f"Top 10 longest words: {', '.join(self.ten_longest_words)}",
            f"Top 10 shortest words: {', '.join(self.ten_shortest_words)}",
            "\nTop 10 longest sentences:\n",
            *self.ten_longest_sentences,
            "\nTop 10 shortest sentences:\n",
            *self.ten_shortest_sentences,
            f"\nNumber of palindrome words: {self.number_of_palindrome_words}",
            f"Top 10 longest palindrome words: {', '.join(self.ten_longest_palindrome_words)}",
            f"Top 10 shortest palindrome words: {', '.join(self.ten_shortest_palindrome_words)}",
            f"Is the whole text a palindrome? (without whitespaces and punctuation marks): {'Yes' if self.is_text_a_palindrome else 'No'}"
            f"\nThe reversed text:\n {self.reversed_text}",
            f"\nThe reversed text but the character order in words kept intact:\n {self.reversed_text_with_saved_words}",
            f"\nAnalyzed in {self.analyzing_time}ms\n\n",
        ]

        return "\n".join(result)
