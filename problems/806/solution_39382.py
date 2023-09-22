def colisao(ret1,ret2):
    """Funcao que dado 2 retangulos, determina se havera colisao entre eles"""
    if ret1[2] <= ret1[4]:
        return True
    else:
        return False