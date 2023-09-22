def conta_frases(frase):
	'''Função retorna a quantidade de frases que 
    um texto possui.String-->Int'''
    if('...' in frase):
         return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+str.count(frase,'...')-3
    else:
    	return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')