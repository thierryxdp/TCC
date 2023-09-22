def colchao(medidas,H,L):
    '''Verifica se é possível passar um colchao por uma porta, dadas as medidas do colchao e a altura e a largura da porta. list, int->bool'''
    if medidas[0]>=L or medidas[1]<=H or medidas[2]<=H:
        return True
    elif medidas[0]>=L or medidas[1]<=L or medidas[2]<=L:
        return True
    else:
        return False