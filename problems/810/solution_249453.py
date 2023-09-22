def inverte(frase):
    ''' '''
    minusculo=frase.lower()
	lista= minusculo.split()
	lista.reverse()
	",".join(lista)
    return lista