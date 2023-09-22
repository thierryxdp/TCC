def colchao(medidas,H,L):
    '''Retorna se é possível ou não passar um colchão de medidas A,B,C pela porta de largura L e altura H
    list,int,int->bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=H and C<=L:
        return True
    if (C<=L and B<=H) or (B<=H and A<=L):
        return True
    if (A<=L and C<=H) or (B<=L and C<=H):
        return True
    else:
        return False