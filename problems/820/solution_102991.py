def posLetra(string,letra,n):
    if n > str.count(string,letra):
        return -1
    posicao = string.find(letra)
    while posicao >= 0 and n > 1:
        posicao = str.find(letra,posicao + 1)
        n -= 1
    return posicao