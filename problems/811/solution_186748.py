def colchao (A,B,C,H,L):
    '''funcao que retorne True se o colchao passa e False se nao passa'''
    if (A+B+C)<(H*L):
        return True
    else:
        return False