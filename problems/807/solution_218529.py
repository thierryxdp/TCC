def conta_frases(texto):
	'''Função que conta um numero de frases que aparece em um texto'''
	'''str->int'''
	ponto = str.count(texto,'.') 
	interrogacao = str.count(texto,'?') 
	exclamacao = str.count(texto,'!')
	trespontos = str.count(texto,'...')  
	return ponto -3 *trespontos+trespontos +exclamacao+interrogacao