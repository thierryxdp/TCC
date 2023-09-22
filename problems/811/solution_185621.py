def colchao(medidas, H, L):
    """ e """
    if (medidas[2] <= H) and (medidas[0] <= L):
    	return True
    elif (medidas[1] <= L) and (medidas[0] <= H):
        return True
    else:
        return False