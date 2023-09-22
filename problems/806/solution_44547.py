#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    l1x = ret1[0]
    l1y = ret1[1]
    r1x = ret1[2]
    r1y = ret1[3]
    l2x = ret2[0]
    l2y = ret2[1]
    r2x = ret2[2]
    r2y = ret2[3]

    if (l1x == r1x or l1y == r1y or l2x == r2x or l2y == r2y):
        return False


    if (l1x > r2x or l2x > r1x):
        return False

    if (r1y < l2y or r2y < l1y):
        return False

    else:
        return True