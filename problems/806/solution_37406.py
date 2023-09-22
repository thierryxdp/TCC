#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1 = (x1, x2, y1, y2)
    ret2 = (x3, x4, y3, y4)   
    if max(x1, x2) < min(x3, x4) and max(y1, y2) < min(y3, y4)\
    or max(x3, x4) < min(x1, x2) and max(y3, y4) < min(y1, y2):
        return True
    else:
        return False