def colchao(medidas,H,L):
    '''função que retorna de acordo com as medidas se o
    colchao passará ou não pela porta'''
    if medidas[1]<=H or medidas[1]<=L :
        return True
    else:
        return False