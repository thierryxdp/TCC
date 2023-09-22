def maiores(lista,n):
    if n not in lista:
        lista.append(n)
    lista.sort()
    i=lista.index(n)
    c=lista.count(n)
    return lista[i+c:]