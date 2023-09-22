def colchao(medidas, H, L): 
    """função que define se colchão passa pela porta
	de acordo com as medidas do mesmo.
    list, int, int -> bool"""

	[A, B, C] = medidas
    if A and B > H and L:
        return False

    else:
        return True