def colchao(medidas, H, L):
    '''Funçao que retorna a possibilidade de se passar um colchao de certas dimensoes por uma
    porta de dimensoes H e L. List, int int -- bool'''
    if L>=medidas[0] and H>=medidas[1]:
        return True
    elif H>=medidas[0] and L>=medidas[2]:
        return True
    else:
        return False