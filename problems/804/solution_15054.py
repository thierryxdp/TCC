def filtra_pares(tupla):
    '''calcule uma função que receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original. tupla-->tupla.''''
    tupla [0] = (x,)
    tupla [1] = (y,)
    tupla [2] = (z,)
    tupla [3] = (w,)
    if (x % 2) == 0:
        return (x)
    elif (y % 2) == 0:
        return (y)
    elif (z % 2) == 0:
        return (z)
    elif (w % 2) == 0:
        return (w)
    else:
        return ()