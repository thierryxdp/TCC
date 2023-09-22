def colchao (medidas,h,l):
    '''...'''
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    
    if (comprimento_colchao>altura_colchao):
        if (largura_colchao>1):
            return False
        elif (largura_colchao<1):
            return True
        else:
            return True