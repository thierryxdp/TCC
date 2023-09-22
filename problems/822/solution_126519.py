def repetidos(lista):
    '''Função que retorna o número de vezes que um elemento 
    da lista dada na entrada é igual ao elemento anterior
    list -> int'''
    e = lista
    i = 0 
    n = 0
    while i <len(e):
        if int(e[i-1]) == int(e[i]):
            n = n + 1 
        i = i + 1
    return n