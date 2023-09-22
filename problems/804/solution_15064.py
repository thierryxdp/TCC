def filtra_pares(tupla):
    '''calcule uma função que receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original. tupla-->tupla.''''
    tupla [0] = (x,)
    tupla [1] = (y,)
    tupla [2] = (z,)
    tupla [3] = (w,)
    if ((x % 2) = 0) and ((y % 2) = 0) and ((z % 2) = 0) and ((w % 2) = 0):
        return  (sorted (x,y,z,w))
    elif (x % 2) = 0 and (y % 2) = 0 and (z % 2) = 0:
        return (x,y,z)
    elif (x % 2) = 0 and (y % 2) = 0:
        return (x,y)
    elif (x % 2) = 0:
        return (x,)
    else:
        return ()