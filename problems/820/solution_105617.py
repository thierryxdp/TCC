def posLetra(string,letra,n):
    indice = 0
    contador = 0
    while indice < len(string):
        if letra in string[indice]:
        contador += 1
            indice += 1
        if contador == n:
            return indice
        if contador != n:
            return -1