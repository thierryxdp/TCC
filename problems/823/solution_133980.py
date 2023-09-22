def faltante(L:list)->int:
    L.sort()
    x = 0
    while x < len(L):
        if L[x] != x+1:
            break
        x += 1
    return x+1