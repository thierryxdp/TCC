def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1 = tuple (x1, y1, x2, y2)
    ret2 = tuple (x3,y3,x4,y4)
    x1 - x2, y1 - y2,x1 - x2,y1 - y2 = ret1
    x3 - x4, y3 - y4,x3 - x4,y3 - y4 = ret2