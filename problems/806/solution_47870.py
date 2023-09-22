#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2, xd2, yd2 = ret2
	if ye2>=xe1 and ye2<=xd1 and xe2>=ye1 and xe2<=yd1 or yd2>=xe1 and yd2<=xd1 and xd2>=ye1 and xd2<=yd1:
		return True
    return False
# segunda etapa - calculo do resultado