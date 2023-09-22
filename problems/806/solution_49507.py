def colisao(coord1,coord2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x0=coord1[0]
    y0=coord1[1]
    x1=coord1[2]
    y1=coord1[3]
    x2=coord2[0]
    y2=coord2[1]
    x3=coord2[2]
    y3=coord2[3]

    if x0<=x2<=x1 and y0<=y2<=y1:
        colidiu=1
    elif x1>=x3>=x0 and y1>=y4>=y0:
        colidiu=1
    else:
        colidiu=0
    return colidiu==1