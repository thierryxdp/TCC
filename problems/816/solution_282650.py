def maiores(lista,n):
    lista.append(n)
    lista.sort(lista)
    return lista[n:]