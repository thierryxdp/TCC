def colchao(medidas,H,L):
    '''
        onde medidas=[A, B, C]
    '''
    if medidas[1]<= H and medidas[0]<= L:
        return True
    if medidas[2]<= H and medidas[0]<= L:
        return True
    else:
        return False