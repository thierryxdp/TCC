def maiores(lista_numeros, n):
    '''
    '''
    
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    posicao = int(list.index(lista_numeros, n))
    del lista_numeros[:posicao + 1]
    return(lista_numeros)