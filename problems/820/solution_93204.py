def posLetra(frase,letra,n):
    y = 0
    x = 0
    while z < len(frase):
        while x < n:
            if frase[y] == letra:
                x = x + 1
            y = y + 1
        z = z + 1
    if x == n:
        return y-1
    if x < n:
        return -1