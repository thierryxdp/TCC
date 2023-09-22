def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista=lista[lista.index(n):]
    return lista