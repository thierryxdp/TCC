def colchao(medidas,H,L):
    altura = medidas[1:2:]
    largura = medidas[2:3:]
    grossura = medidas[:1]
    return altura[0] <= H and grossura[0] <= 36