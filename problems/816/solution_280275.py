def maiores(lista,n):
    if n not in lista:
        lista.append(n)
        lista.sort()
        p = lista.index(n)
        listaMaiores = lista[p+1:]
        return listaMaiores
    else:
        lista.sort()
        p = lista.index(n)
        listaMaiores = lista[p+1:]
        return listaMaiores