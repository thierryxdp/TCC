def faltante(pecas):
    '''Função que identifica qual numero da peça que está faltando dada 
    uma lista de numeros como entrada.
    lista -> int'''
    
    lista = []
    indice = 0
    
    pecas.sort()
    
    while indice < (len(pecas)-1):
        if pecas[indice+1] - pecas[indice] > 1: 
        	return indice+1
        indice +=1