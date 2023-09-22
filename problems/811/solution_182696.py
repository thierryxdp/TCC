def colchao(medidas,H,L):
    '''retorna se True se o colchão passa e False se não passa'''
    if medidas[0]*medidas[1]<=H*L or medidas[0]*medidas[2]<=H*L or medidas[1]*medidas[2]<=H*L:
        return True
    else:
        return False