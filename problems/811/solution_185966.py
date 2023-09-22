def colchao(medidas, H, L):
    A = medidas[0]
	B = medidas[1]

    if (A > H or B > H) and (A > L or B > L):
        return False
    else:
        return True