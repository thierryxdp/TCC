"""Retorna o número de frases.
str->int"""
def conta_frases(frases):
    if '.':
        return 1
    
    if not '.' and '!':
        return 2
    if not '.' and '!' and '?':
        return 3
	else:
    	return 4