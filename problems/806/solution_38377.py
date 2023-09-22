#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1x=ret1[:1]
    ret1y=ret1[2:3]
    ret1w=ret1[4:5]
    ret1h=ret1[6:7]
    ret2x=ret2[:1]
    ret2y=ret2[2:3]
    ret2w=ret2[4:5]
    ret2h=ret2[6:7]
    if re2x<=ret1x+ret1w
    and ret2x+ret2w>=ret1x 
    and ret2y<=ret1y+ret1h
    and ret2y+ret2w>=ret1y
        return not(True)