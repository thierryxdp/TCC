def faltante(L):
    l = list(range(max(L)+1))
    L.sort()
    l.pop(0)
    L.append(max(L)+2)
    l.append(max(l)+1)
    i=0
    while L[i] == l[i]:
        l.pop(i)
        L.pop(i)
    return l[0]