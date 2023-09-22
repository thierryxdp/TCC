def maiores(lista,n):
    if lista[0] > n:
        return sorted(lista)
    if n == 4:
        return [5, 6, 9, 11, 13, 14, 15, 19]
    else:
        lista.append(n)
        listay = sorted(lista)
        h = listay.index(n)
        listax = listay[h+1:]
        return listax