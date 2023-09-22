def colchao(medidas,H,L):
    ''' define se um colchao de medidas [a,b,c] passa por
    	uma porta de medidas H e L.
        list, int, int --> bool '''
    medidas = list()
    altura = H
    largura = L
    if medidas[1] <= H or medidas[1] <= L:
        return True
    elif medidas[2] <= H or medidas[2] <= H:
        return True
    elif medidas[1] > H or medidas[2] > L:
        return False
    else:
        return False