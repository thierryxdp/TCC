def colisao(ret1,ret2):
        '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se há colisão entre os 2 retângulos e False, caso contrário.
     tuple, tuple --> bool'''
    x1 = tuple(ret1)[0]
    y1 = tuple(ret1)[1]
    x2 = tuple(ret1)[2]
    y2 = tuple(ret1)[3]
    x3 = tuple(ret2)[0]
    y3 = tuple(ret2)[1]
    x4 = tuple(ret2)[2]
    y4 = tuple(ret2)[3]

    if (int(x2)<int(x3)) or (int(x4)<int(x1)) or (int(y2)<int(y3)) or (int(y4)<int(y1)):
        return False
    else: 
        return True