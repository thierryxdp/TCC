def colchao(medidas,H,L):
    """Dado um colchao de dimensoes[A,B,C], retorna se é possível que este atravesse uma pota de altura H, e comprimento L
    list,int,int-->bool"""
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