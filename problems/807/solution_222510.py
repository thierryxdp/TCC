def conta_frases(frase):
	'''Função retorna a quantidade de frases que 
    um texto possui.String-->Int'''
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+srt.count(frase,'...')