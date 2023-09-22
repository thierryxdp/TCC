def colchao(medidas,H,L):
    """
    list -> bool"""
    if medidas[1]<=H or medidas[2]<=H:
        return True 
    else:
        return False