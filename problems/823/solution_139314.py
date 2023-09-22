def faltante(l):
    N = len(l) + 1
    x = -1
    for i in range(1, N):
        if i not in l:
            return i
    return max(l) + 1