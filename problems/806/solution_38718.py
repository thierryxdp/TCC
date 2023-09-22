#Start your python function here
def colisao(t1,t2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if (t2[2] < t1[0] or t1[2] < t2[0]) and (t2[3] < t1[1] or t1[3] < t2[1]):
        return False
    else:
        return True