def colchao(medidas,H,L):
    ''' verifica se o colchão passará pela porta'''
    verifica_H = bool(medidas[1] <= H or medidas[2] <= H)
    verifica_L = bool(medidas[1] <= L or medidas[2] <= L)
    return verifica_H or verifica_L