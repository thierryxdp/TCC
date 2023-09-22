#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

 	xi1= int(ret1[0])
    yi1= int(ret1[1])
    xs1= int(ret1[2])
    ys1= int(ret1[3])

    xi2= int(ret2[0])
    yi2= int(ret2[1])
    xs2= int(ret2[2])
    ys2= int(ret2[3])

    if (xs1-xi2) >= 0 and (ys1-yi2) >= 0 and (xs2-xi1) >= 0 and (ys2-yi1) >= 0:
        return True

    else:
        return False