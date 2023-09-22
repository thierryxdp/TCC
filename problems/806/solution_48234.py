def colisao(xi1, yi1, xs1, ys1, xi2, yi2, xs2, ys2 ):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    
    ret1 = [xi1, yi1, xs1, ys1]
    ret2 = [xi2, yi2, xs2, ys2]
    
    if ret1[2] < ret2[2] or ret2[2] < ret1[2] or ret1[3] < ret2[3] or ret2[3] < ret1[3]:
        return True 
    else:
        return False