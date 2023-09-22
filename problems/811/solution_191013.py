def colchao(medidas, H, L):
    
    """Funcao define se colchao passa pela porta."""
    "list, float, float--> bool"
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False