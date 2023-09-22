def faltante(l):
    N = max(l)
    x = -1
    for i in range N:
        if i not in l:
            return i