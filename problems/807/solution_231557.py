import re
def conta_frases(texto):
    """Retorna o número de frases de uma string;
    str -> int"""
    if '!' or '?' or '...' or '... ' or '.' or '. ' in texto:
        return len(texto.split())