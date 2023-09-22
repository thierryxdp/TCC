def colchao(medidas,H,L):
    '''Funcao que confirma se o colchao passa ou nao pela 
    porta, os valores devem ser ditos em cm seguindo a 
    ordem, espessura A, largura B, comprimento C, altura da 
    porta H, largura da porta;
    [A,B,C],H,L->bool'''
    
    medidas=[]
    areac=(2*medidas[0]*medidas[1])+(2*medidas[1]*medidas[2])+(2*medidas[0]*medidas[2])
    Areap=H*L
    
    if areac>Areap:
        return False
    if areac<Areap:
        return True