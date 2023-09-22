def colchao(medidas,H,L):
    """funçaõ que determina se João consegue passar o colchão pelas portas de sua casa. int, int, int -> bool"""
    if medidas[0]<=H and medidas[1]<=L:
        return True
    elif medidas[1]<=H and medidas[0]<=L:
        return True
    elif medidas[0]<=L and medidas[2]<=H:
        return True
    elif medidas[1]<=L and medidas[2]<=H:
        return True
    else:
        return False