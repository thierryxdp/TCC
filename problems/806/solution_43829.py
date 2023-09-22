def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    return not (float (ret2 [2]) < float (ret1[0]) or float (ret1 [2]) < float (ret2 [0])) and not (float(ret2[3]) < float (ret1 [1]) or float (ret1 [2]) < float (ret2[1]))