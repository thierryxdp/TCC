def conta_frases(texto):
    '''retorna o numero de frases de entrada
    srt->int'''
    ponto= str.count(texto,'.')
    reticencias=str.count(texto,'...')
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    frases=ponto+reticencias+interrogacao+exclamacao
    
   	if reticencias >= 1:
        return frases-reticencias*3
    	else:
        	return frases