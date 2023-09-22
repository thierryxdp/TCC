#Start your python function here
def colisao(primeiro,segundo):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
	[largura1, altura1, x1, y1] = medidas(primeiro)
    [largura2, altura2, x2, y2] = medidas(segundo)
    if x2 >= x1 and x2 <= x1 + largura1:
        if y2 >= y1 and y2 <= y1 + altura1:
            return True
    if x1 >= x2 and x1 <=x2 + largura2:
        if y1 >= y2 and y1 <= y2 + altura2:
            return True
    return False


def medidas(ret):
    [x1, y1, x2, y2] = ret;
    return [x2 - x1, y2 - y1, x1, y2]