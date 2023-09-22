#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    A = (ret1[0]==ret2[0]) and (ret1[1]==ret2[1]) and (ret1[2]==ret2[2]) and (ret1[3]==ret2[0])
    B = (ret1[0]==ret2[0]) or (ret1[1]==ret2[1]) or (ret1[2]==ret2[2]) or (ret1[3]==ret2[0])
    if A == false:
        return A
    else:
        return B