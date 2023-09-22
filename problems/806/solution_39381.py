def colisao([ret1],[ret2]):
    """Funcao que dado 2 retangulos, determina se havera colisao entre eles"""
    ret1= tup[0], tup[2], tup[4], tup[6]
    ret2= tup[1], tup[3], tup[5], tup[7]
    if tup[2] <= tup[4]:
        return True
    else:
        return False