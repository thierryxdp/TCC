def posLetra(string, letra, numero):
    posicao = string.find(letra)
    while posicao >= 0 and n > 1:
        posicao = string.find(letra, posicao + 1)
        n -= 1
    return posicao