def filtra_pares(a, b, c, d):
  '''recebe quatro parametros e retorna apenas os que sao pares, em forma de tupla.
    int, int, int, int --> none to four int'''
    pares = []
    for e in (a, b, c, d):
        if e % 2 == 0:
            pares.append(e)
    return pares