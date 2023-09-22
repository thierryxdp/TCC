def posLetra(s, letra, n):
    posicao = s.find(letra)
    while posicao >= 0 and n > 1:
        posicao = s.find(letra, posicao + 1)
        n -= 1
    return posicao