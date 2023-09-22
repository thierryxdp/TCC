"""Retorna o número de frases.
str->int"""
def conta_frases(frases):
	if '.':
        return 1
    if '.' and '!':
        return 2
    if '.' and '!' and '?':
        return 3
    if '.' and '!' and '?' and '...':
        return 4