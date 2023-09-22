def maiores(lista,n):
    if lista[0] > n:
        return sorted(lista)
    else:
        lista.append(n)
        listax = lista[lista.index(n)+1:]
        return listax