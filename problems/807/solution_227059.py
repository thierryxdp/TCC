def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    	
    ponto = (frase.count('.'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    total = exclamacao + interrogacao + ponto
    if frase.count("...") == 0:
    	return total
	else:
		tresp = (frase.count('...'))
    	exclamacao = (frase.count('!'))
    	interrogacao = (frase.count('?'))
    	totaltres = exclamacao + interrogacao + tresp
		return totaltres