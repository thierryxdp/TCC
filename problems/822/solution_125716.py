def repetidos(lista):
    """recebe uma lista de numeros e retorna o numero de vezes em que um elemento
    da lista e igual ao elemento anterior
    list -> int"""
    
    i = 1
    j = 0
    
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            j += 1
            
        i =+ 1
        
    return j