def conta_frases(texto):
	"""Funcao que calcula a quantidade de frases dentro de um texto dado como parametro
    	str->int"""
    return str.count(texto,'.') + str.count(texto,'?') + str.count(texto,'!')