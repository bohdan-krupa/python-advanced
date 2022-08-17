from timer import timer
from text_analyzer import TextAnalyzer


@timer
def analyze() -> None:
    ta = TextAnalyzer('text.txt')

    print('Statistical information:')
    print('Number of characters:', len(ta.text))
    print('Number of words:', len(ta.words))
    print('Number of sentences:', len(ta.sentences))
    print('Frequency of characters:', ta.characters_frequency)
    print('Distribution of characters as a percentage of total:', ta.characters_frequency_as_percentage_of_total)
    print('Average word length:', ta.average_word_length)
    print('The average number of words in a sentence:', ta.average_number_of_words_in_sentence)
    print('Top 10 most used words:', ', '.join(ta.top_10_most_used_words))
    print('Top 10 longest words:', ', '.join(TextAnalyzer.top_10_longest(ta.words)))
    print('Top 10 shortest words:', ', '.join(TextAnalyzer.top_10_shortest(ta.words)))
    print('\nTop 10 longest sentences:\n', '\n'.join(TextAnalyzer.top_10_longest(ta.sentences)))
    print('\nTop 10 shortest sentences:\n', '\n'.join(TextAnalyzer.top_10_shortest(ta.sentences)))
    print('\nNumber of palindrome words:', len(ta.palindrome_words))
    print('Top 10 longest palindrome words:', ', '.join(TextAnalyzer.top_10_longest(ta.palindrome_words)))
    print('Top 10 shortest palindrome words:', ', '.join(TextAnalyzer.top_10_shortest(ta.palindrome_words)))
    print(
        'Is the whole text a palindrome? (without whitespaces and punctuation marks):',
        'Yes' if TextAnalyzer.is_palindrome(ta.text_without_spaces_and_punctuation) else 'No'
    )
    print('\nThe reversed text:\n', ta.text[::-1])
    print('\nThe reversed text but the character order in words kept intact:\n', ta.reversed_text_with_saved_words)


if __name__ == '__main__':
    analyze()
