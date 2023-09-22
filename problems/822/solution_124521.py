def repetidos(lista):
    """Dado uma lista de números, retorna quantas vezes o nú-
    mero de vezes que um elemento da lista é igual ao elemento
    anterior; 
    list -> int"""
    x = 0 
    vezes = 0 
    a = lista[x]
    b = lista[x+1]
    while x < len(lista) :
        if a == b : 
            vezes = vezes + 1 
        x = x + 1
        
    return vezes