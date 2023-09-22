def repetidos(lista):
    """funcao que recebe uma lista de numeros e retorna o numero de vezes em que um elemento é igual ao elemento anterior
	list -> int"""
    
    i = 0
    j = 1 
    
    while len(lista) > j:
        if lista[j] == lista[j-1]:
            lista.count(lista[j])
            i += 1
        j += 1
    
    return i