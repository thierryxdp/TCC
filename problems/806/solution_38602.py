def colisao(ret1,ret2):
    """a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool"""
    
    x1, y1, x2, y2 = ret1
    
    x3 = ret2[0]
    y3 = ret2[1]
    x4 = ret2[2]
    y4 = ret2[3]

    if x2 >= x3 and y2 >= y3:
        return True