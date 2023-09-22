def colchao(medidas,h,l):
    '''função que calcula se um colchão passa por uma porta, medidas do colchão em ordem crescente
    list,int,int----> bool'''
    if medidas[2] <=h or medidas[1]<= l or medidas [1]<= h:
        return True
    else:
        return False