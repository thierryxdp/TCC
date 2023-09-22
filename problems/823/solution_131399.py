def faltante(lista):
    """Ao fornecer uma lista com N - 1 inteiros enumerados de 1 a N
    cuja numeração representa cada peça do jogo, retorna a peça faltante.
    
    list -> int"""
    
    list.sort(lista)
    indice = 0
    comparativo = list(range(1,len(lista)+2))

    if lista[0] != 1: 
        return 1

    while indice < len(lista):
    	    	
        if lista[indice] < comparativo[indice]:
        indice += 1
        return comparativo[indice]
        
        if lista[indice] == comparativo[indice]:                                                 
        return comparativo[indice]
    	indice += 1
        

    if lista[0] == 1:
        return lista[-1]+1