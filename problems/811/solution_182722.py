def colchao(medidas,H,L):
    '''retorna se True se o colchão passa e False se não passa'''
    if medidas[1]<=H and medidas[2]<=L and medidas[1]*medidas[2]<=H*L:
        return True
    else:
        return False