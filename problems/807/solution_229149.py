def conta_frases(frase):
    '''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''    
	list = []
	pontuacao=['...','!','?','.']
	z = frase.split('...')
	for x in z:
   		c = x.split('!')
    for v in c:
        	b = v.split('?')
        	for n in b:
            	m = n.split('.')
            	list.append(m)
	return len(list)