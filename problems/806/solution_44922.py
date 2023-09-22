#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if (('ret1_x' > 'ret2_x')or('ret1_x' < 'ret2_x')or('ret1_y' > 'ret2_y')or('ret1_y' < 'ret2_y')):
        return True or False