def maiores(lista,m):
    L1 = list(lista)
    L1.append(m)
    L1.sort()
    i = L1.index(m)
    return L1[i:]