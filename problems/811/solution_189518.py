def colchao(medidas,H,L):
    'dados as medidas de um colchao e a altura e largura de uma porta, retorne se o colchao passa pela porta.list,int,int->bool'
    if medidas[0]<=L and medidas[1]<=H :
        return true
    elif medidas[1]<=L and medidas[0]<=H :
        return true
    else:
        return false