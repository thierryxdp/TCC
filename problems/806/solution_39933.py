#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    r1x1=ret1[0]
    r1x2=ret1[1]
    r1y1=ret1[2]
    r1y2=ret1[3]
    r2x1=ret2[0]
    r2x2=ret2[1]
    r2y1=ret2[2]
    r2y2=ret2[3]
    
    return((r2x1>r1x2 and r2y1>r1y2) or (r1x1>r2x2 and r1y1>r2y2))== False