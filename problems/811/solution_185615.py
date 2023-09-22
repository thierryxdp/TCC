def colchao(medidas, H, L):
    """Retorna se o colchão passa ou não pela porta
       Entrada: list, int, int
       Saida: bool
    """
    if medidas[1]>H and medidas[2]>L:
        return False
    
    if medidas[1]>H or medidas[2]>L:
        return True
    else 
    return True