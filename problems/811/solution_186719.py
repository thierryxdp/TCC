def colchao (medidas, H,L):
    '''funcao que retorne True se o colchao passa e False se nao passa'''
    if medidas > H*L:
        return False
    else:
        return True