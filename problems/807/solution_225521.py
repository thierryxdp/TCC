def conta_frases(texto):
    """função que recebe texto e conta as frases.
    str--> int"""
	contagem1 = texto.count('.')
	contagem2 = texto.count('!')
	contagem3 = texto.count('?') 
	contagem4 = texto.count('...')
	
	return contagem1 - contagem4 + contagem2 + contagem3