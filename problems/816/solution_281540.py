def maiores(lista,n):
    a = lista.append(n)
    b = lista.sort()
    c = str(lista)
    d = c.split(n)
    return lista[d:]