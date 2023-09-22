def repetidos(lista):
    '''
    Função que recebe como entrada uma lista de números
    e retorna o número de vezes que um elemento da lista 
    é igual ao elemento anterior.
    
   	list -> int
    
    '''
    p = 1
    c = 0
    while p < len(lista):
        if lista[p] == lista[p-1]:
            c = c + 1
        p = p + 1
    return c