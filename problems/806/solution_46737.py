def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    a = (ret1[0],)
    b = (ret1[1],)
    c = (ret1[2],)
    d = (ret1[3],)
    e = (ret2[0],)
    f = (ret2[1],)
    g = (ret2[2],)
    h = (ret2[3],)
    if (g>a and h>b and c>e and d>f) or (c>e and d>f and g>a and h>b):
        return True
    else:
        return False