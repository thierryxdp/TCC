def colchao(medidas,H,L):
    '''
        onde medidas=[A, B, C]
    '''
    if medidas[1]<= H and medidas[0]<= L:
        return True
    if medidas[2]<= H and medidas[0]<= L:
        return True
    if medidas[1]<= L and medidas[0]<= H:
        return True
    if medidas[2]<= L and medidas[1]<= H:
        return True
    else:
        return False