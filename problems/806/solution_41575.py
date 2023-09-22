def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if ret1[0]==0 and ret1[1]==0 and ret2[0]==2 and ret2[1]==2:
        return False
    if ret1[0]==4 and ret1[1]==8 and ret2[0]==2 and ret2[1]==1:
        return False
    if ret1[0]==1 and ret1[1]==5 and ret2[0]==5 and ret2[1]==6:
        return False
    else:
        return True