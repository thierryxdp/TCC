#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2, xd2, yd2 = ret2

# segunda etapa - calculo do resultado
    if (xe2<=xe1<=xd2 or xe2<=xd1<=xd2 or xe1<=xe2<=xd1 or xe1<=xd2<=xd1) and (yd2>=ye1>=ye2 or yd2>=yd1>=ye2 or yd1>=ye2>=ye1 or yd1>=ye2>=ye1):
        return True
    else:
        return False