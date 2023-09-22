def faltante(l):
    l = list.sort(l)
    n = l[-1]
    ls = list(range(1, (n+1)))
    for i in ls:
        if i not in l:
            return i