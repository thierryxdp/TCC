def colchao(medidas, H, L):
    # medidas = [A, B, C]
    # H = altura porta
    # L = largura porta
    medidas.remove(min(medidas))
    if min(medidas) < max([H,L]):
        return True
    else:
        return False