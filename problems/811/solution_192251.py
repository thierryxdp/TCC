def colchao(medidas,H,L):
    ''' Função que calcula se é possível fazer o colchão passar da porta através das medidas da porta e do colchão;
    list,int,int->bool'''
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False