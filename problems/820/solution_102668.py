def posLetra(texto, letra, n):
    posição = str.find(texto,letra)
    while posição >= 0 and n > 1:
        posição = str.find(texto,letra, posição + 1)
        n -= 1
    return posição