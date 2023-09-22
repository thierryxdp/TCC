def conta_frases(texto):
	'''...'''
	ponto = str.count(texto,'.') 
	interrogacao = str.count(texto,'?') 
	exclamacao = str.count(texto,'!')
	trespontos = str.count(texto,'.')  
	return -3 * trespontos + trespontos + exclamacao + interrogacao