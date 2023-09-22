def posLetra(string, letra, numero):
    posicao = string.find(letra)
    while posicao >= 0 and numero > 1:
        posicao = string.find(letra, posicao + 1)
        numero -= 1
    return posicao