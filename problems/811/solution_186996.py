def colchao(medidas,H,L):
    '''A função calcula se o colchão vai passar pela prota dados as medidas de entrada H e L, dados suas altura e comprimento'''
    '''list,int,int -> str'''
    if medidas [1] <= H:
        return True
    if medidas [1] <= L:
        return True 
    else:
        return False