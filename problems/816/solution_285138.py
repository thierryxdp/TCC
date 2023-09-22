def maiores(lista,n):
    x=lista[:]
    list.clear(x)
    for k in lista:
        if k>n:
            x.append(k)
            list.sort(x)
    return x