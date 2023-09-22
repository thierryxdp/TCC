def conta_frases(texto):
    """função que recebe texto e conta as frases.
    str--> int"""
	contagem1 = texto.count('.')  #separa texto pelos pontos
	contagem2 = texto.count('!')  #separa texto pelos pontos de exclamação
	contagem3 = texto.count('?') #separa texto pelo ponto de interrogação
	contagem4 = texto.count('...') #conta quantas reticências tem na frase
	
	return contagem2 - contagem4 + contagem1 + contagem3