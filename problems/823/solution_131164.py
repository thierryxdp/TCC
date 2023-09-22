def faltante(pecas):
    pecas.sort()
    N = len(pecas) + 1
    todas_pecas = (range(1, N + 1))
    indice = 0
    peca_que_falta = 1
    
    while todas_pecas[indice] in pecas:
        indice += 1
        peca_que_falta += 1

    return peca_que_falta