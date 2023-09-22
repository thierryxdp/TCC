def colchao(medidas,H,L):
    """Recebe as medidas do colchao e da porta e define se o colchao
     passaria ou nao pela porta. 
     entradas float, float, float, int, int --> saida bool"""
    B = medidas[1]
    if B < H:
        return True
    if B > H:
        return False
    if B > H:
        if B < L:
            return True