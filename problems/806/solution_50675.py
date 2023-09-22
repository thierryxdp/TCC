#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1= tuple(ret1)
    ret2= tuple(ret2)
    if(ret1[0]<= ret2[0] <= ret1[2] or ret1[0] <= ret2[2] < ret1[2]):
        return True 
    else: 
        return False