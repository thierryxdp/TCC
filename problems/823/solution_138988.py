def faltante(l):
    l = l.sort()
    n = l[-1]
    for i in range(1, (n+1)):
        if i not in l:
            return i