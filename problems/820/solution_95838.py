def posLetra(frase,letra,n):
    contador = 0
    i = 0
    while i in range(len(frase)):
        if f[i] == letra:
            contador = contador + 1
            if contador == n:
                return i
        i = i+1
    return -1