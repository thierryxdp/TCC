def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple(float,float,float,float), tuple(float,float,float,float) --> bool'''
    
    xinfret1 = ret1[0]
    yinfret1 = ret1[1]
    xsupret1 = ret1[2]
    ysupret1 = ret1[3]
    xinfret2 = ret2[0]
    yinfret2 = ret2[1]
    xsupret2 = ret2[2]
    ysupret2 = ret2[3]
    
    if not (xsupret2 < xinfret1 or xsupret1 < xinfret2) and not (ysupret2 < yinfret1 or ysupret1 < yinfret2):
        return True
    else:
        return False