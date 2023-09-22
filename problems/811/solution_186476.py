def colchao(medidas,H,L):
    '''dadas as medidas de um colchão, a altura H e a largura L de uma porta, calcula se o colachão passa por aquela porta
    list,int,int-->bool'''
    if medidas[0]<=L and medidas[2]<=H:
        return True
    elif medidas[1]<=H or (medidas[0]>=L and medidas[1]>=H):
        return True
    else:
        return False