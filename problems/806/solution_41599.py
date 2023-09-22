def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool''' 
    x1 = int(ret1[0])
    x2 = int(ret2[0])
    y1 = int(ret1[1])
    y2 = int(ret2[1])
    L1 = int(ret1[2])
    L2 = int(ret2[2])
    A1 = int(ret1[3])
    A2 = int(ret2[3])
    delta_x = math.abs(x1-x2)
    delta_y = math.abs(y1-y2)
    L = 0
    A = 0
    if (x1 < x2):
        L = L1
    else:
        L = L2
    if (y1 < y2):
        A = A1
    else:
        A = A2
    if (delta_x >= L or delta_y >= A):
        return False
    else:
        return True