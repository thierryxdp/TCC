"""Retorna o número de frases.
str->int"""
def conta_frases(frases):
    if '.':
        return 1 or 2 or 3 or 4
    if '.' or '!':
        return 2
    if '.' or '!' or '?':
        return 3
    if '.' or '!' or '?' or '...':
        return 4