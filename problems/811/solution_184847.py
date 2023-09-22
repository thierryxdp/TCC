def colchao(medidas,H,L):
    """..."""
    a = medidas[0]
    b = medidas[1]
    
    if (H<=a and L<=b) or (H<=b and L<=A):
        return True
    else:
        return False