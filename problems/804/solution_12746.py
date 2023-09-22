def filtra_pares(x,y,z,w):
    '''Função que recebe uma tupla com quatro elementos inteiros e retorne uma nova tupla contendo apenas os elementos pares da tupla original
    tupla, tupla, tupla, tupla -> tupla'''
    restox = x%2
    restoy = y%2
    restoz = z%2
    restow = w%2
    if restox == 0:
        if restoy == 0:
            if restoz == 0:
                if restow == 0:
                    return x, y, z, w