def colchao(medidas, H, L):
    # medidas = [A, B, C]
    # H = altura porta
    # L = largura porta
    medidas.remove(min(medidas))
    if (medidas[0] > max(medidas)) or (medidas[1] > max(medidas)):
        return False
    else:
        return True