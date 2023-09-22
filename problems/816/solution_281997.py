def maiores(lista,n):
    lista.append(n)
    lista = lista.sort()
    return lista[n+1:]