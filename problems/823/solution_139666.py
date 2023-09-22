def faltante(lista):
    i = 0
    c = 0
    n = len(lista) + 1
    while i <= n+1:
        if i not in range(1,n +1):
            c = c + i
        i = i + 1
    return c