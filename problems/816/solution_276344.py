def maiores(lista,n):
    '''Retorna uma lista com todos os números da lista dada maiores que n'''
    '''list,int -> list'''
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    del lista[:posicao+1]
    return lista