def posLetra(texto, letra, n):
    posicao = str.find(texto,letra)
    while posicao >= 0 and n > 1:
        posicao = str.find(texto,letra, posicao + 1)
        n -= 1
    return posicao