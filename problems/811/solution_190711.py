def colchao(m, H, L):
    """Essa função verifica se o colchão passa pela porta dada a altura H e largura L. int -> bool"""
    [A, B, C] = m
    if A and B > H and L:
        return False
    else:
        return True