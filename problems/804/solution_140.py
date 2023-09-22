def filtra_pares(a, b, c, d):
  '''recebe quatro parametros e retorna apenas os que sao pares, em forma de tupla.
    int, int, int, int --> none to four int'''
    elementos = (a, b, c, d)
    pares = tuple(filter(lambda x: (x % 2 == 0), elementos))
    return pares