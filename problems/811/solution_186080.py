def colchao(medidas, H, L):
    altura, largura, comprimento = medidas
    if comprimento > L:
        return False
    if largura > H:
        return False
    return True