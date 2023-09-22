def posLetra(frase,letra,n):
    y = 0
    while y < len(palavra):
        if letra in palavra[y]:
            y = y + 1
    if y == n:
        return y
    if y != n:
        return -1