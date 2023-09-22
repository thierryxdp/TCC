def posLetra(frase,letra,n):
    y = 0
    while y < len(frase):
        if letra in frase[y]:
            y = y + 1
    if y == n:
        return y
    if y != n:
        return -1