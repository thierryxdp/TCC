def colisao(ret1,ret2):
    """Funcao que dado 2 retangulos, determina se havera colisao entre eles"""
    ret1=[R1x,R3x,R5x,R7x]
    ret2=[R2x,R4x,R6x,R8x]
    if ret1[R5x] <= ret1[R3x]:
        return True
    else:
        return False