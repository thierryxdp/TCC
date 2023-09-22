def colchao(medidas,H,L):
    '''função que retorna true caso um colchão passe por uma porta ou false caso não passe.
    entrada: list, int, int
    saída: string'''
    if H > medidas[2] and L > medidas[1]:
        return 'True'
    elif H >= medidas[1] and L > medidas[0]:
        return 'True'
    else:
        return 'False'