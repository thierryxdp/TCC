def quant_palavras(frase):
	"""A função recebe uma string e retorna o número de palavras dessa string.
	string -> int"""
	e1 = frase.strip()
	e2 = e1.split()
	return len(e2)