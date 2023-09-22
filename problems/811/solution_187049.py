def colchao(medidas,H,L):
    """qa"""
    
    a = medidas[0]
    b= medidas [1]
    c= medidas[2]
    if c<= H and c<= L:
        return True
    elif b=< H and b=< L:
        return True
    else:
        return False