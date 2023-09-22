import re
def conta_frases(texto):
    """Retorna o número de frases de uma string;
    str -> int"""
    return len(re.split('!', texto))