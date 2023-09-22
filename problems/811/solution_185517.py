def colchao(medidas, H, L):
    # medidas = [A, B, C]
    # H = altura porta
    # L = largura porta
    medidas.remove(min(medidas))
    if max(medidas) < max([H,L]):
        return False
    else:
        return True