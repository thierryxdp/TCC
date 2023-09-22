def repetidos(lista):
    """Dado uma lista de números, retorna quantas vezes o nú-
    mero de vezes que um elemento da lista é igual ao elemento
    anterior; 
    list -> int"""
    x = 0 
    vezes = 0 
    while x < len(lista):
        if lista[x] == lista[x-1] : 
            vezes = vezes + 1 
        x = x + 1
        
    return vezes