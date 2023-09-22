def colchao(medidas,H,L):
    '''Recebe as medidas de um colchão e altura e largura de uma porta e informa se o colchão passa pela porta; lista, float, float -> bool'''
    a, b, c = medidas[0], medidas[1], medidas[2]
    if (a <= L) and ((b <= H) or (c <= H):
                     return True
    else:
                     return False