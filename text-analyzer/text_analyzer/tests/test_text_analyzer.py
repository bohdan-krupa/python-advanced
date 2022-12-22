from ..text_analyzer import TextAnalyzer
from tests.consts import (
    EXPECTED_CHARACTERS_FREQUENCY,
    EXPECTED_CHARACTERS_FREQUENCY_AS_PERCENTAGE_OF_TOTAL,
    EXPECTED_REVERSED_TEXT,
    EXPECTED_REVERSED_TEXT_WITH_SAVED_WORDS,
    EXPECTED_TEN_LONGEST_SENTENCES,
    EXPECTED_TEN_SHORTEST_SENTENCES,
    EXPECTED_TEXT_WITHOUT_SPACES_AND_PUNCTUATION,
    EXPECTED_TOP_10_MOST_USED_WORDS,
)


def test_characters_frequency(text_analyzer: TextAnalyzer):
    characters_frequency = text_analyzer.characters_frequency
    assert characters_frequency == EXPECTED_CHARACTERS_FREQUENCY


def test_characters_frequency_as_percentage_of_total(text_analyzer: TextAnalyzer):
    characters_frequency_as_percentage_of_total = (
        text_analyzer.characters_frequency_as_percentage_of_total
    )

    assert (
        characters_frequency_as_percentage_of_total
        == EXPECTED_CHARACTERS_FREQUENCY_AS_PERCENTAGE_OF_TOTAL
    )


def test_average_word_length(text_analyzer: TextAnalyzer):
    average_word_length = text_analyzer.average_word_length
    assert average_word_length == 5.38


def test_average_number_of_words_in_sentence(text_analyzer: TextAnalyzer):
    average_number_of_words_in_sentence = (
        text_analyzer.average_number_of_words_in_sentence
    )
    assert average_number_of_words_in_sentence == 13.57


def test_top_10_most_used_words(text_analyzer: TextAnalyzer):
    top_10_most_used_words = text_analyzer.top_10_most_used_words
    assert top_10_most_used_words == EXPECTED_TOP_10_MOST_USED_WORDS


def test_palindrome_words(text_analyzer: TextAnalyzer):
    palindrome_words = text_analyzer.palindrome_words
    assert palindrome_words == ["non", "non", "esse", "a", "a", "a", "esse"]


def test_text_without_spaces_and_punctuation(text_analyzer: TextAnalyzer):
    text_without_spaces_and_punctuation = (
        text_analyzer.text_without_spaces_and_punctuation
    )
    assert (
        text_without_spaces_and_punctuation
        == EXPECTED_TEXT_WITHOUT_SPACES_AND_PUNCTUATION
    )


def test_reversed_text_with_saved_words(text_analyzer: TextAnalyzer):
    reversed_text_with_saved_words = text_analyzer.reversed_text_with_saved_words
    assert reversed_text_with_saved_words == EXPECTED_REVERSED_TEXT_WITH_SAVED_WORDS


def test_is_palindrome():
    is_palindrome = TextAnalyzer.is_palindrome("TesttseT")
    assert is_palindrome == True


def test_is_palindrome():
    is_palindrome = TextAnalyzer.is_palindrome("Testtset")
    assert is_palindrome == False


def test_report(text_analyzer: TextAnalyzer):
    report = text_analyzer.report

    assert report.number_of_characters == 629
    assert report.number_of_words == 95
    assert report.number_of_sentences == 7
    assert report.frequency_of_characters == EXPECTED_CHARACTERS_FREQUENCY
    assert (
        report.distribution_of_characters
        == EXPECTED_CHARACTERS_FREQUENCY_AS_PERCENTAGE_OF_TOTAL
    )
    assert report.average_word_length == 5.38
    assert report.average_words_in_sentence == 13.57
    assert report.ten_most_used_words == EXPECTED_TOP_10_MOST_USED_WORDS

    assert report.ten_longest_sentences == EXPECTED_TEN_LONGEST_SENTENCES
    assert report.ten_shortest_sentences == EXPECTED_TEN_SHORTEST_SENTENCES
    assert report.number_of_palindrome_words == 7
    assert report.ten_longest_palindrome_words == ["esse", "non", "a"]
    assert report.ten_shortest_palindrome_words == ["a", "non", "esse"]
    assert report.is_text_a_palindrome == False
    assert report.reversed_text == EXPECTED_REVERSED_TEXT
    assert (
        report.reversed_text_with_saved_words == EXPECTED_REVERSED_TEXT_WITH_SAVED_WORDS
    )
