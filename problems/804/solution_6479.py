def filtra_pares(x):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas elementos pares'''
    x1,x2,x3,x4 = x
    if (x1%2) == 0:
        y=(x1,)
    if (x2%2) == 0:
      y=(x2,)+y[1:]
    if (x3%2) == 0:
        y=(x3,)+y[1:]
    if (x4%2) == 0:
      y=(x4,)+y[1:]
    return y