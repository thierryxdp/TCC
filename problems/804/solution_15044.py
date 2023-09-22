def filtra_pares (x,y,z,w):
    '''calcule uma função que receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original. tupla-->tupla.''''
    elementos= x, y, z, w
    if (x % 2) == 0:
        return sorted(x)
    elif (y % 2) == 0:
        return sorted(y)
    elif (z % 2) == 0:
        return sorted(z)
    elif (w % 2) == 0:
        return sorted(w)