def insere(lista,n):
    '''
    adiciona n, mantendo a lista ordenada
    list,n -> list
    '''
    lista1= lista.sort(0:n-1)
    lista1= lista.append(n)
    lista2= lista.sort(n+1:)
    lista= lista1 + lista2
    return lista