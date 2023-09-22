def colchao(medidas, H, L):
    """Funcao que retorna se o colchão passa por uma porta de medidas H,L."""
    if medidas[1]<=L and medidas[2]<=H:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=L and medidas[2]<=H:
        return True
    else:
        return False