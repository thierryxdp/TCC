#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if r1x1<=r2x1<=r1x2 or r1x1<=r2x2<=r1x2:
        if r1y1<r2y1<=r1y2 or r1y1<=r2y2<=r1y2:
            return True 
        return False