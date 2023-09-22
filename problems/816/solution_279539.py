def maiores(lista,n):
    if n in lista:
        return lista
    else:
        lista.append(n)
        sorted(lista)
        x = lista.index(n)
        return lista[x:]