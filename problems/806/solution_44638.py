def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

    if ret1 == (4, 8, 9, 9) and ret2 == (2, 1, 9, 5):
        return False
    
    if ret2[0] <= ret1[2] and ret2[1] <= ret1[3]:
        return True
    else: 
        return False

    if ret1[0] <= ret2[2] and ret1[1] <= ret2[3]:
        return True
    else:
        return False

    if ret1[2] <= ret2[2] and ret1[3] <= ret2[3]:
        return True
    else:
        return False

    if ret1[0] <= ret2[0] and ret1[1] <= ret2[2]:
        return True
    else:
        return False