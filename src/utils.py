import unicodedata
import re

def normalize_text(text):
    """
    Normaliza el texto eliminando acentos y convirtiéndolo a minúsculas.

    Args:
        text (str): El texto a normalizar.

    Returns:
        str: El texto normalizado.
    """
    text = text.lower() # Convertir a minusculas
    text = unicodedata.normalize('NFD', text) # Descomponer caracteres acentuados
    # Remover caracteres de acento y otros modificadores
    text = ''.join([c for c in text if unicodedata.category(c) != 'Mn'])
    # Retornar el texto normalizado
    return text


def matches_any(text, patterns):
    """
    Comprueba si el texto coincide con alguno de los patrones proporcionados.

    Args:
        text (str): El texto de entrada a comprobar.
        patterns (list): Una lista de patrones de expresión regular.

    Returns:
        bool: True si alguno de los patrones coincide con el texto normalizado, False en caso contrario.
    """
    norm = normalize_text(text)
    return any(re.search(p, norm) for p in patterns)
