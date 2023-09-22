"""Retorna o número de frases.
str->int"""
def conta_frases(frases):
    if '.' or '!' or '?' or '...':
        return 4
    elif '.':
        return 1
    elif '.' or '!':
        return 2
    elif '.' or '!' or '?':
        return 3