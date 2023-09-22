def conta_frases(texto):
	'''...'''
	ponto = str.count(texto,'.') 
	interrogacao = str.count(texto,'?') 
	exclamacao = str.count(texto,'!')
	trespontos = str.count(texto,'.')  
	return trespontos + interrogacao + exclamacao + trespontos