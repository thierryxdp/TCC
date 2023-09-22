def colchao(medidas,H,L):
    """retorna a informação de se o colchao definido pela entrada medidas passa pela porta de largura L e altura H; list, int, int -> bool"""
    porta=H*L
    lado_1=medidas[0]*medidas[1]
    lado_2=medidas[0]*medidas[2]
    lado_3=medidas[2]*medidas[1]
    if porta>=lado_1:
        return True
    elif porta>=lado_2:
        return True
    elif porta>=lado_3:
        return True
    else:
        return False