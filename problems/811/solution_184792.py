def colchao(medidas,H,L):
    """ função que, dadas as medidas de um colchão e de uma
    porta, diz se o colchão passa ou não pela porta.
    List, Int, Int -> Bool"""
    
    A,B,C = medidas
    
    if C < H and B < L:
        return True
    elif A < H and B < L:
        return True
    else:
        return False