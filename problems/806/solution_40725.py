def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xi1, yi1, xs1, ys1 = ret1
    xi2, yi2, xs2, ys2 = ret2
    if xi2 > xs1 :
        return False 
    elif xi2 < xs1 :
        return True