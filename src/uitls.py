import unicodedata
import re

def normalize_text(text):
    """
    Normalize text by converting to lowercase, removing accents, 
    and stripping diacritics.

    Args:
        text (str): The input text to normalize.

    Returns:
        str: The normalized text.
    """
    text = text.lower() # Convert to lowercase
    text = unicodedata.normalize('NFD', text) # Decompose characters
    # Remove accents and diacritics
    text = ''.join([c for c in text if unicodedata.category(c) != 'Mn'])
    # Return the normalized text    
    return text

def matches_any(text, patterns):
    """
    Check if the normalized text matches any of the provided patterns.

    Args:
        text (str): The input text to check.
        patterns (list): A list of regex patterns to match against.

    Returns:
        bool: True if any pattern matches the normalized text, False otherwise.
    """
    norm = normalize_text(text)
    return any(re.search(p, norm) for p in patterns)
