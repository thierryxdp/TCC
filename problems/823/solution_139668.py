def faltante(lista):
    i = 0
    c = 0
    n = len(lista) + 1
    while i <= n:
        if i not in range(0,n +1):
            c = c + i
        i = i + 1
    return c