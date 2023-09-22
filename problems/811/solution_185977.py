def colchao(medidas,H,L):
    """Determina se um colcão com dimensões contidas na lista
    'medidas' pode passar uma porta de altura H e largura L;
    list, int, int -> bool"""
    if H > L and medidas[0]<= H and medidas[1] <= H or medidas[0]<= H and medidas[2]<= H or medidas[1]<= H and medidas[2]<= H:
            return True
    if H < L and medidas[0]<= L and medidas[1] <= L or medidas[0]<= L and medidas[2]<= L or medidas[1]<= L and medidas[2]<= L:
            return True
    else:
        return False