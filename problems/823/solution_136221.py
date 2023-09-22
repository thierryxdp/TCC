def faltante(lista):
    """função que recebe uma lista com 1-N números inteiros e retorna o número que esta faltando dessa lista
	list -> int"""
    
    lista.sort()
    i = 0
    
    while i < len(lista):
        if i+1 == lista[i]:
            i += 1
        
        else:
            return i+1
    
    return i+1