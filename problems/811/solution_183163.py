def colchao(medidas,H,L):
    '''...'''
    if L >= medidas[0] and H >= medidas[1] or H >= medidas[0] and L >= medidas[1]:
        return True
    else:
        return False