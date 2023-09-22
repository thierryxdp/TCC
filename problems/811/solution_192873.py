def colchao(medidas,H,L):
    '''funçao que calcula se o colchao consegue passar pel a porta
    list,int,int-->bool'''
    if (medidas[0] <= L and medidas[1] <=H) or (medidas[0] <= H and medidas[1] <=L):
        return true 
    else:
        return false