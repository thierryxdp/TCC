def colchao(medidas,H,L):
    """..."""
    A = medida[0]
    B = medida[1]
    
    if (B <= H and A <= L) or (B <= L and A <= H):
        return True 
    else:
        return False