def conta_frases(frase):
	"""conta quantas frases tem e retorna com um numero 
   str>int"""
	return frase.count('.')+frase.count('!')+frase.count('?')-2*frase.count('...')