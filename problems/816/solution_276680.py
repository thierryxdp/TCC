def maiores(lista,n):
    clone=lista[:]
    if n in lista:
        clone.sort()
        del clone[:n-1]
        lista = clone
        return lista
    else:
        lista.clear()
        return lista