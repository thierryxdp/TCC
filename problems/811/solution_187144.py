def colchaomedidas,H,L):
    '''funcao que dadas as medidas( dimensoes) de um colchao,a altura H e a largura L de uma porta retorna True ou False se o colchao puder passar pela porta
    lista,int,int->bool'''
    if (medidas [0]<=H and medidas[1]<=L) or(medidas[0]<=L and medidas[1]<=H):
        return True
    elif (medidas[0]<=H and medidas[2]<=L) or(medidas[0]<=L and medidas[2]<=H):
         return True
    elif (medidas[2]<=H and medidas[1]<=L) or(medidas[2]<=L and medidas[1]<=H):
        return True
    else:
        return False