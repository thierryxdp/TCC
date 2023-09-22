def maiores(lista, n):
    '''A função retornará uma lista com apenas os números maiores que (n).
    
    dados de entrada -> lista, int
    dados de saída -> lista'''
    
    list.append(lista,n)
    list.sort(lista)
    posicao = list.index(lista,n)
    
    return lista[posicao-1:]