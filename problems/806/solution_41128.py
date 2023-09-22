#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2,  xd2, yd2 = ret2
    if xe2<=xd1 and xe2>=xe1 and ye2<=yd1 and ye2>=ye1 or xd1>=xe2 and xd1<=xd2 and yd1>=ye2 and yd1<=yd2:
        return True
    else:
        return False