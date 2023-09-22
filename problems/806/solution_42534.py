def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x_iesq1, y_iesq1, x_sdir1, y_sdir1 = ret1
    x_iesq2, y_iesq2,  x_sdir2, y_sdir2 = ret2
    return (x_sdir2>=x_iesq1>=x_iesq2 and y_iesq1==y_iesq2) or (x_iesq2<=x_sdir1<=x_sdir2 and y_sdir1==y_sdir2) or (x_iesq1==x_sdir2 and y_iesq2<=y_iesq1<=1y_sdir2) or (x_iesq2==x_sdir1 and y_iesq1<=y_iesq2<=y_sdir2)