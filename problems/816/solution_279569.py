def maiores(lista,n):
    if lista[0] > n:
        return sorted(lista)
    else:
        lista.append(n)
        listay = sorted(lista)
        h = listay.index(n)
        listax = listay[h+1:]
        return listax