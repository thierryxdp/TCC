def maiores(lista,n):
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]