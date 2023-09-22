def colchao (A,B,C,H,L):
    '''funcao que retorne True se o colchao passa e False se nao passa'''
    if (A and B)> (H and L) or (A and C)>(H and L) or (B and C)>(H and L):
        return True
    else:
        return False