def conta_frases(frase):
    '''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''    
	list = []
	pontuacao=['...','!','?','.']
	z = frase.split('...')
	for x in z:
    	v = frase.split('!')
    for c in v:
    	b = frase.split('?')
	for n in b:
    	m = frase.split('.')
	return len(m) - 1