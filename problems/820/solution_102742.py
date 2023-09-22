def posLetra(texto, letra, n):
    posicao = texto.find(letra)
    while posicao >= 0 and n > 1:
        posicao = texto.find(letra, posicao + 1)
        n -= 1
    return posicao