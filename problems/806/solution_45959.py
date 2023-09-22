#Start your python function here
def colisao(x1,y1,x2,y2,x3,y3,x4,y4):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
ret1 = x1,y1,x2,y2
    ret2 = x3,y3,x4,y4
    if x1 >= x3 or y1 >= y3:
        return True
    if x2 >= x3 or y2 >= y3:
        return True
    if x1 == x3 or y1 == y3:
        return True
    if x2 == x3 or y2 == y3:
        return True
    if x2 == x4 or y2 == y4:
        return True
    else:
        return False