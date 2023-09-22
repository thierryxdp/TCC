#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
   	return not(str(ret2)[2]<str(ret1)[0] or str(ret1)[2]<str(ret2)[0])and not(str(ret2)[1]<str(ret1)[1] or str(ret1)[3]<str(ret2)[1]):