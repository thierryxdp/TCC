def colchao(medidas,H,L):
    '''retorna True se o colchão passa e False se não passa'''
    if medidas[0]<=H and medidas[1]<=L:
        return True
    elif medidas[0]<=H and medidas[2]<=L:
        return True
    elif medidas[1]<=H and medidas[0]<=L:
        return True
    elif medidas[1]<=H and medidas[2]<=L:
        return True
    elif medidas[2]<=H and medidas[0]<=L:
        return True
    elif medidas[2]<=H and medidas[1]<=L:
        return True