def faltante(pecas):
    pecas.sort()
    n = len(pecas) + 1
    pecasJuntas = range(1, n + 1)
    posicao = 0
    faltando = 1
    
    while pecasJuntas[posicao] in pecas:
        posicao = posicao + 1
        faltando = faltando + 1

    return faltando