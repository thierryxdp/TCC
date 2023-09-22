'''
A função informa se o colchão passa pela porta.
'''
def colchao(medidas,H,L):

    if medidas[1] <= H or medidas[2] <= L:
        return True
    else:
        return False