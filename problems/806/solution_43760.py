def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x1, y1, x11, y11 = ret1
    x2, y2,  x22, y22 = ret2
    return x1>=x2 or x2<=x11 or x1>=x22 or x22<=x11 or y1>=y2 or y2<=y11 or y1>= y22 or y22<= y11