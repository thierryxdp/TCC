def maiores(lista_n,n):
    '''
    Funçao que dada uma lista de numeros inteiros e um numero n,
    retorna outra lista que contenha todos os numeros maiores do
    que n
    list-> list
    '''
    list.append(lista_n, n)
    list.sort(lista_n, reverse=True)
    pos=list.index(lista_n,n)
    del lista_n[pos:]
    
    return lista_n