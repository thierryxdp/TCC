def colchao(medidas,H,L):
    '''Funcao que confirma se o colchao passa ou nao pela 
    porta, os valores devem ser ditos em cm seguindo a 
    ordem, espessura A, largura B, comprimento C, altura da 
    porta H, largura da porta;
    [A,B,C],H,L->bool'''
    
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    areac=(2*A*B)+(2*B*C)+(2*A*C)
    Areap=H*L
    
    if areac>Areap:
        return False
    else areac<Areap:
        return True