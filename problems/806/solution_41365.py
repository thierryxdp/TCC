#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xe1= ret1[0]
    ye1= ret1[1]
    xd1= ret1[2]
    yd1= ret1[3]
    
    xe2= ret2[0]
    yed= ret2[1]
    xd2= ret2[2]
    yd2= ret2[3]
    
    if xe1>xd2 and ye1>yd2:
            return false
	if xd1<xe2 and yd1<ye2:
            return false
	else:
        true