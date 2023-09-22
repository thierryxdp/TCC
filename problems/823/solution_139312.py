def faltante(l):
    N = len(l) + 1
    x = -1
    for i in range(N):
        if i not in l:
            x = i
    return x