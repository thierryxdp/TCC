def colchao(medidas,H,L):
    '''retorna True se o colchão passa e False se não passa'''
    if medidas[0]*medidas[1]<=L*H:
        return True
    elif medidas[0]*medidas[2]<=L*H:
        return True
    elif medidas[1]>L and medidas[1]>H:
        return False
    else:
        return False