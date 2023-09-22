def colchao(medidas,H,L):
    """Dada as medidas de um colchão com dimensões A x  B x C, e as
    dimensões de um porta de altura(H) e largura(L), a função calcula
    se é possível passar o colchão(AxBxC) pela porta (HxL).
    As medidas do colchão devem ser colocadas entre colchetes[];
    list,int,int --> bool"""
    if medidas[0] <= H and medidas[1] <= L:
        return True
    if medidas[0] <= H and medidas[2] <= L:
        return True
    if medidas[1] <= H and medidas[0] <= L:
        return True
    if medidas[1] <= H and medidas[2] <= L:
        return True
    if medidas[2] <= H and medidas[0] <= L:
        return True
    if medidas[2] <= H and medidas[1] <= L:
        return True
    else:
        return False