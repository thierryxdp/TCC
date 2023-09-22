def inverte(frase):
    ''' '''
   
    minusculo=frase.lower()
	lista= minusculo.split()
	lista.reverse()
	return str(lista).strip('[]')