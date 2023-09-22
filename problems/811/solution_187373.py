def colchao(medidas, H, L):
    if (medidas[0] <= H or medidas[0] <= L) and (medidas[1] <= H or medidas[1] <= L) and (medidas[2] <= H or medidas[2] <= L):
        return True
    else:
        return False