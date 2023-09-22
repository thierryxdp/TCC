#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
	
    x1 = ret1[0]
    y1 = ret1[1]
    x2 = ret1[2]
    y2 = ret1[3]
    
    x3 = ret2[0]
    y3 = ret2[1]
    x4 = ret2[2]
    y4 = ret2[3]

    if not(x4 < x1 or x2 < x3) and not(y4 < y1 or y2 < y3):
        return True
    else:
        return False