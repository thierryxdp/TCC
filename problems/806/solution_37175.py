def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xa1 = a[0]
    ya1 = a[1]
    xa2 = a[2]
    ya2 = a[3]
    xb1 = b[0]
    yb1 = b[1]
    xb2 = b[2]
    yb2 = b[3]
    if not (xb2 < xa1 or xa2 < xb1) and not (yb2 < ya1 or ya2 < yb1):
        return True
    else:
        return False