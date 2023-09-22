def colchao(medidas, H, L):
    alturaColchao = medidas[1]
    larguraColchao = medidas[2]
    if alturaColchao <= H and larguraColchao <=L:
        return True
    return False