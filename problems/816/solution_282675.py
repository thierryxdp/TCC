def maiores2(lista,n):
    lista.append(n)
    lista.sort()
    indice=list.index(lista,n)
    return lista[indice:]