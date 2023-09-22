def insere(listanumeros,n):
    '''Insere um numero n na lista mantendo a ordem crescente. list-->list'''
    listanumeros.append(n)
    list.sort(listanumeros)
    return listanumeros