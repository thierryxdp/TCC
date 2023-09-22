def colchao(medidas,H,L):
    """retorna a informação de se o colchao definido pela entrada medidas passa pela porta de largura L e altura H; list, int, int -> bool"""
    L1=medidas[0]
    L2=medidas[1]
    if (H>L1 and L>L2) or (H>L2 and L>L1):
        return True
    else:
        return False