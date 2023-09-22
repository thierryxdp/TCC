def repetidos(lista):
    """Retorna o número de vezes que um elemento da lista é igual ao elemento anterior.
    lista --> int"""
    
    vezes = 0
    i = 1
    
    while i < len(lista):
        if lista[i-1] == lista[i]:
            vezes = vezes + 1
        i = i + 1
        
    return vezes