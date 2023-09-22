def colchao(medidas,H,L):
    '''indica se o colchao de dimencoes(medidas) passara pela porta de dimensoes(H e L).'''
    altura = medidas[1:2:]
    largura = medidas[2:3:]
    return altura[0] <= H or largura[0] <= L