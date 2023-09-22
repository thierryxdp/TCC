def maiores(lista,n):
    if lista[0] > n:
        return sorted(lista)
    else:
        lista.append(n)
        listay = sorted(lista)
        listax = listay[lista.index(n)+1:]
        return listax