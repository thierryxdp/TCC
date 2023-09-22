def faltante(pecas):
	
    '''retorna qual o numero da peca do quebra cabeca esta 
    faltando, de acordo com a lista inserida como parametro
    list -> int'''
    
    list.sort(pecas)

    i = 0

    while i < len(pecas)-1:
        if (pecas[i] - pecas[i+1]) != -1:
            return pecas[i]+1
		i = i + 1
    
    if pecas[0] != 1 and len(pecas) != 1:
        return 1
    
    if pecas[0] = 1 and len(pecas) = 1:
        return 2
    
    if len(pecas) == 1:
        return pecas[0]-1
    
    return pecas[len(pecas)-1] + 1