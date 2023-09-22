def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''


    a, b, c, d = ret1
    w, x,  y, z = ret2
    
    if a<w<b:
        return True
    if a<x<b:
        return True
    if a<y<b:
        return True
    if a<z<b:
        return True
    else:
        return False