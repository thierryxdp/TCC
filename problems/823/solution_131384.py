def faltante(L):
    '''função que dada uma lista L retorna o numero que está
    faltando na sequencia'''
    contador = 0
	if 1 not in L:
        return 1
    elif len(L) == 1:
        return 2
    elif len(L) == L[-1]:
        return L[-1] + 1
    else:
    	while L[contador] == contador + 1:
        	contador = contador + 1
    	return contador + 1