def colisao(ret1,ret2):
    '''A funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, x1, y1, x2 e y2 representando as 
     coordenadas dos vertices inferior esquerdo e superior direito do primeiro retangulo e x3, y3, x4, y4 representando as
     coordenadas dos vertices inferior esquerdo e superior direito do segundo retangulo e devolve True se ha colisao entre
     os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x1 = ret1[0]
    y1 = ret1[1]
    x2 = ret1[2]
    y2 = ret1[3]
    x3 = ret2[0]
    y3 = ret2[1]
    x4 = ret2[2]
    y4 = ret2[3]
    if (x2<x3) or (x4<x1) or (y2<y3) or (y4<y1):
        return 0==1
    else:
        return 0==0