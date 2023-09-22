def faltante(L):
    '''função que dada uma lista L retorna o numero que está
    faltando na sequencia'''
    contador = 1
	if 1 not in L:
        return 1
    else:
    	while L[contador] != (L[contador - 1] + 1):
        	contador = contador + 1
    	return L[contador] + 1