def faltante1(pecas):
    lp = pecas[:]
    lp.sort()
    contador = 0
    peca = -1
    while (contador < len(lp)):
        if (lp[contador] == (contador + 1)):
            contador = contador + 1
        else:
            peca = contador + 1
            contador = len(lp)
    if (peca == -1):
        peca = len(lp) + 1
    return peca