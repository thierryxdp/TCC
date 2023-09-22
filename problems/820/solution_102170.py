def posLetra(string,letra,n):
    posicao = string.find(letra)
    while posicao >= 0 and n > 1:
        a = string.find(letra,posicao+1)
        n = n - 1
    return posicao