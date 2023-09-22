def maiores(lista,n):
    lista.append(n)
    lista.sort()
    indice=lista.index(lista,n)
    return lista[indice+1:]