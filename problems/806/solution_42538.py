def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xq1, yq1, xd1, yd1 = ret1
    xq2, yq2,  xd2, yd2 = ret2
    return ((xd2>=xq1 and xd1>=xq2) and (yq1==yq2 or yd1==yd2 or yq2==yd1 or yq1==yd2)) or ((yd2>=yq1 and yd1>=yq2) and (xq1==xq2 or xd1==xd2 or xq2==xd1 or xq1==xd2))