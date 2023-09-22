def conta_frases(frase):
	'''Função que recebe um texto e conta o número de frases que aparecem nesse texto,
	considerando que cada frase é terminada em ponto final, exclamação, interrogação ou 
	reticências.
	Entrada: string
	Saída: int'''
	frase=frase.replace('!','.')
	frase=frase.replace('?','.') 
	frase=frase.replace('...','.')
	return frase.count('.')