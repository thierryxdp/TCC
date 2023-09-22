def colchao(medidas, H, L):
    altura = medidas[0]
    comprimento = medidas[1]
    largura = medidas [2]
    if (comprimento>H):
        if (largura>L):
            return False
        else:
            return True
        elif (largura<L):
            return True
        else:
            return True