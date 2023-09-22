def colisao(primeiro,segundo):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    [altura1, largura1, x1, y1] = medidas(primeiro)
    [altura2, largura2, x2, y2] = medidas(segundo)
    if x2 > x1 and x2 < x1 + largura1:
        if y2 > y1 and y2 < y1 + altura1:
            return True
    return False


def medidas(ret):
    [x1, y1, x2, y2] = ret;
    return [x2 - x1, y2 - y1, x1, y2]