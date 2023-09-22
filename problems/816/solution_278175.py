def maiores(lista,n):
    ''' '''
    if n not in lista:
        listaSomada = lista + [n]
        listaSomada.sort()
        maioresQ = listaSomada[lista.index(n)+1:]
        return maioresQ
    else:
        lista.sort()
        maioresQ = lista[lista.index(n)+1:]
        return maioresQ