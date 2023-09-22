def posLetra(frase,letra,n):
    y = 0
    x = 0
    while y < len(frase):
        if letra in frase[y]:
            x = x + 1
        y = y + 1
    if x == n:
        return x
    if x != n:
        return -1