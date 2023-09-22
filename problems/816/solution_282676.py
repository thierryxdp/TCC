def maiores(lista,n):
    lista.append(n)
    lista.sort()
    indice=list.index(lista,n)
    return lista[indice:]