def colchao (medidas, H, L) :
    """Funcao que retorna se um colchão passa pela porta de casa considerando as dimensões de medida, H e L"""
    if (H > L) and (medidas[0] <= L) and (medidas[1] <= H) :
        return True
    else :
        return False