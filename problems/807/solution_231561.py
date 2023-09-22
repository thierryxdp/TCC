import re
def conta_frases(texto):
    """Retorna o número de frases de uma string;
    str -> int"""
    adada = ['!', '?', '...', '.']
    if adada in texto:
        return len(texto.split(adada))