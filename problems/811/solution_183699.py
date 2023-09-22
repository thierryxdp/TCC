def colchao(medidas,h,l):
    '''Retorna se é possivel passar um colchão atraves de uma porta'''
    if h >= medidas[1]:
        return True
    if h >= medidas[2]:
    	return True
    else:
        return False