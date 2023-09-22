#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    for j in range(2):
        for i in range(2):
            if ret1[j]==ret2[i]:
                return 'True'
    for j in range(2,4):
        for i in range(2,4):
            if ret1[j]==ret2[i]:
                return 'True'