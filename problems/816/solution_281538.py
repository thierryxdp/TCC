def maiores(lista,n):
    a = lista.append(n)
    b = lista.sort()
    c = str(lista)
    d = c.find(n)
    return lista[d:]