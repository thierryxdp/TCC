def colchao(medidas,H,L):
    '''retorna se True se o colchão passa e False se não passa'''
    medidas=[A,B,C]
    if B*C<H*L:
        return True
    else:
        return False