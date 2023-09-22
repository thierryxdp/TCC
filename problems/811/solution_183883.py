def colchao(medidas,H,L):
    """funçao"""
    if medidas[0]*medidas[1]*medidas[2]<=H*L:
        return False
    else:
        return True