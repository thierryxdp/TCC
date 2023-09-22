def colchao(medidas,H,L):
    '''colchao'''
    A,B,C= medidas
    return min(B,C)<=max(H,L)