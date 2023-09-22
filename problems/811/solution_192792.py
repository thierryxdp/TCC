def colchao(medidas,H,L):
    ''' verifica se o colchão passará pela porta'''
    verifica_H = bool(medidas[0] >= H or medidas[1] >= H)
    return verifica_H