def colchao(medidas, H, L):
    # medidas = [A, B, C]
    # H = altura porta
    # L = largura porta
    medidas.remove(min(medidas))
    if (medidas[0] > L and medida[0] > H) or (medidas[1] > L and medidas[1] > H):
        return False
    else:
        return True