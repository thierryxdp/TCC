def colchao(medidas,H,L):
    ''' verifica se o colchão passará pela porta'''
    verifica_H = bool(medidas[1] <= H or medidas[2] <= H)
    return verifica_H