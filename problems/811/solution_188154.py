def colchao(medidas,H,L):
    altura=[H]
    largura=[L]
    if medidas[1:2] > altura and medidas[1:2] > largura and medidas[2:] > altura and medidas[2:] > largura:
        return True
    else:
        return False