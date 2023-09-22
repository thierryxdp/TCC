def colchao(medidas, H, L):
    altura, largura, comprimento = medidas
    if largura > L and comprimento > H:
        return False
    return True