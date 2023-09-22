def acima_da_media(lista,n):
    lista.insert(n,n)
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]