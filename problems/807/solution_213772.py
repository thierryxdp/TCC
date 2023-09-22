import re

def conta_frases(texto):
    """Recebe um texto e retorna a quantidade de frases nele"""
    return len(re.compile("[\.\!\?]+").split(texto)) - 1