def colchao(medidas,H,L):
    """retorna se um colchão de medidas [A,B,C] passa através de uma porta
    de altura H e largura L de entrada
    list, int, int --> bool"""
    if medidas[1]<=H:
        return True
    elif medidas[1]<=L:
        return True
    elif medidas[2]<=H:
        return True
    elif medidas[2]<=L:
        return True
    else:
        return False