"""Retorna o número de frases.
str->int"""
def conta_frases(frases):
    if '.':
        return 1
    
    elif '.' and '!':
        return 2
    elif '.' and '!' and '?':
        return 3
	else:
    	return 4