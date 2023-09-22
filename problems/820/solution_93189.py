def posLetra(frase,letra,n):
    y = 0
    x = 0
    while x < n:
        if frase[y] == letra:
            x = x + 1
        y = y + 1
    if x == n:
        return x
    if x != n:
        return -1