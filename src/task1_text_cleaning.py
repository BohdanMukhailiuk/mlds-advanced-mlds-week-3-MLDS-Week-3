"""Task 1: Text Cleaning and Tokenization."""
import re
from typing import List
from nltk.tokenize import word_tokenize


def clean_and_tokenize(text: str) -> List[str]:
    """
    Clean text by removing punctuation, converting to lowercase, and tokenizing.

    Args:
        text (str): The input text string to clean and tokenize.

    Returns:
        List[str]: A list of tokens (words).

    Raises:
        ValueError: If text is None or empty.
        TypeError: If text is not a string.

    Example:
        >>> clean_and_tokenize("Hello, World!")
        ['hello', 'world']
    """
    tokens = ''
    if not text:
        raise ValueError('Input text cannot be empty')
    
    if not isinstance(text, str):
        raise TypeError('Input text must be a string')
    
    if not text.strip():
        raise ValueError('Input text cannot be empty')
    
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = word_tokenize(text)

    return tokens


if __name__ == "__main__":
    example_text = (
        "Cleans the input text by removing punctuation and converting it to lowercase, "
        "then tokenizes it into individual words."
    )
    print(clean_and_tokenize(example_text))

