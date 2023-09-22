def maiores(lista,n):
    if n in lista:
        return lista
    else:
        lista.append(n)
        sorted(lista)
        x = lista.index(n)
        lista.remove(n)
        return lista[x:]