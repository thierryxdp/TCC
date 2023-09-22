def conta_numero(num, mat):
    '''Dado um numero e uma matriz é retornado o numero
    de vezes que o numero aparece na matriz
    int, list------->int'''
    i = 0
    for linha in mat:
        for coluna in linha:
            if coluna == num:
                i += 1
    return i