def colchao (medidas,H,L):
    '''dimensoes do colchao'''
    [A ,B, C] = medidas 
    if A and B > H and L:
        return False
    else:
        return True