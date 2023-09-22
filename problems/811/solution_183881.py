def colchao(medidas,H,L):
    """funçao"""
    if 2*((medidas[0]*medidas[1])+(medidas[1]*medidas[2])+(medidas[0]*medidas[2]))<=H*L:
        return True
    else:
        return False