def faltante(l):
    l = list.sort(l)
    v = l[-1]
    ls = list(range(1, (v+1)))
    for i in ls:
        if i not in l:
            return i