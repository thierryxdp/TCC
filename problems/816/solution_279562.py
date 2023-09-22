def maiores(lista,n):
    if lista[0] > n:
        return sorted(lista)
    else:
        lista.append(n)
        sorted(lista)
        listax = lista[lista.index:]
        return listax