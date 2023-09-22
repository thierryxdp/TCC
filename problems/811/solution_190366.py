def colchao(medidas,H,L):
    '''Uma funcão que calcula se um colchao de medidas A*B*C 
    consegue passar por uma porta com largura L'''
    if medidas[1] <= H or medidas[1] <= L:
        return True
    else:
        return False