def colchao(medidas, H, L):
    # medidas = [A, B, C]
    # H = altura porta
    # L = largura porta
    if min([H, L]) < min(medidas):
        return True
    else:
        return False