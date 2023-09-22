def colchao(medidas, H, L):
    altura, largura, comprimento = medidas
    if largura > H and comprimento > L:
        return False
    return True