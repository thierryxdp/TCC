def colchao(medidas, H, L):
    A = medidas[0]
	B = medidas[1]

    if (A > H and B > H) or (A > L and B > L):
        return False
    else:
        return True