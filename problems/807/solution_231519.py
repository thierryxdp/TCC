import re
def conta_frases(texto):
    """Retorna o número de frases de uma string;
    str -> int"""
    if '!' in texto:
        return len(texto.split('!'))
    elif '?' in texto:
        return len(texto.split('?'))
    elif '...' in texto:
        return len(texto.split('... '))
    elif '. ' in texto:
        return len(texto.split('. '))