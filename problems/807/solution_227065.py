def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    	
    ponto = (frase.count('.'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    total = exclamacao + interrogacao + ponto
    if frase.count("...") == 0:
    	return total
		else if frase.count("...") == 1:
		tresp = (6*(frase.count('...'))) - (frase.count('.'))
    	exclamacao = (frase.count('!'))
    	interrogacao = (frase.count('?'))
    	totaltres = exclamacao + interrogacao + tresp
		return totaltres
    else if (frase.count("...") == 1 and frase.count(".") == 0):
		tresp = (6*(frase.count('...'))) - (frase.count('.'))
    	exclamacao = (frase.count('!'))
    	interrogacao = (frase.count('?'))
    	totaltres = exclamacao + interrogacao + tresp
		return totaltres
    else if (frase.count("...") == 1 and frase.count(".") != 0):
		tresp = (6*(frase.count('...'))) - (frase.count('.'))
    	exclamacao = (frase.count('!'))
    	interrogacao = (frase.count('?'))
    	totaltres = exclamacao + interrogacao + tresp
		return totaltres
    else:
		tresp = (6*(frase.count('...'))) - (frase.count('.'))
    	exclamacao = (frase.count('!'))
    	interrogacao = (frase.count('?'))
    	totaltres = exclamacao + interrogacao + tresp
		return totaltres