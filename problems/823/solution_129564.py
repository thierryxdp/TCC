def faltante(pecas):
    '''Função que identifica qual numero da peça que está faltando dada 
    uma lista de numeros como entrada.
    lista -> int'''
    
    lista = []
    indice = 0
    
    pecas.sort()
    
    if len(pecas)-1 > 1:
    	while indice < (len(pecas)-1):
        	if pecas[indice+1] - pecas[indice] > 1: 
        		return indice+2
        	indice +=1
    if pecas[0] == 1:
        return pecas[-1]+1
    else:
        return pecas[0]-1