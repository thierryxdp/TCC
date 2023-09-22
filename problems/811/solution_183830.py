def colchao(medidas, H, L):
    """Recebe as medidas de um colchão e uma porta, e retorna se o colchão passa
    pela porta ou não"""
    A, B, C = medidas
    if((A <= H and B <= L) or (B <= H and A <= L)):
        return True
    elif((A <= H and C <= L) or (C <= H and A <= L)):
        return True
    elif((B <= H and C <= L) or (C <= H and B <= L)):
        return True
    else:
        return False