#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    r1_x1, r1_y1, r1_x2, r1_y2 = ret1
    r2_x1, r2_y1, r2_x2, r2_y2 = ret2
    if r1_x2 < r2_x1 or r2_x2 < r1_x1 or r1_y2 < r2_y1 or r2_y2 < r1_y1 or r1_x1 > r2_x2 or r2_x1 > r1_x2 or r1_y1 > r2_y2 or r2_y1 > r1_y2:
        return False
    else:
        return True