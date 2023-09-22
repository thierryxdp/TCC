def peca(pecasT,pecas):
    n = 0
    list.sort(pecasT)
    list.sort(pecas)
    while pecasT[n] == pecas[n]:
        n = n + 1
    return n + 1