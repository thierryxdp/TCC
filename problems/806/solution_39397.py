def colisao(ret1,ret2):
    """Funcao que dado 2 retangulos, determina se havera colisao entre eles"""
    ret1=tuple("R1xR3xR5xR7x")
    ret2=tuple("R2xR4xR6xR8x")    
    if ret2[0] >= ret2[1]:
        return True
    else:
        return False