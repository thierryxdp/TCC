def maiores(lista, n):
    lista.append(n)
    lista.sort()
    lista1=lista.index(n)
    return lista[lista1+lista.count(n):]