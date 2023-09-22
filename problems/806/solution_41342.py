def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xi1,yi1,xf1,yf1=ret1
    xi2,yi2,xf2,yf2=ret2
    if xi1<=xf2 and xi1>=xi2 and yi1<=yf2 and yi1>=yi2:
        return True
    elif xf1<=xf2 and xf1>=xi2 and yf1<=yf2 and yf1>=yi2:
        return True
    else:
        return False