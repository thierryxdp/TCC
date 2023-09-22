#Start your python function here
def colisao(r1,r2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if r1[0]>r2[2] or r2[0]>r1[2]:
        return False
    elif r1[1]>r2[3] or r2[1]>r1[3]:
        return False
    else: 
        return True