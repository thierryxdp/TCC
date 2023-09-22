def colchao(medidas, H, L):
    """recebe as medidas do colchão e as medidas da porta e retorna se o colchão passa ou não."""
    if medidas[1] <= H:
        return True
    if medidas[2] <= L:
        return True
    return False