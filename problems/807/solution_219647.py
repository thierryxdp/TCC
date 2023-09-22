"""Retorna o número de frases.
str->int"""
def conta_frases(frases):
    if '.':
        return 1
    elif '.' or '!':
        return 2
    elif '.' or '!' or '?':
        return 3
    elif '.' or '!' or '?' or '...':
        return 4