def dimen_colchao(lista1, H, L):
    """
"""
    if lista1[0] <= L and lista1[1] <= H:
        return True
    elif lista1[1] <= L and lista1[0] <= H:
        return True
    else:
        return False