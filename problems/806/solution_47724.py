#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
	x1_r1, y1_r1, x2_r1, y2_r1 = ret1[0], ret1[1], ret1[2], ret1[3]
	x1_r2, y1_r2, x2_r2, y2_r2 = ret2[0], ret2[1], ret2[2], ret2[3]

	if (x1_r2 >= x1_r1 and x1_r2 <=x2_r1) or (x2_r2 >= x1_r1 and x2_r2 <=x2_r1):
		if (y1_r2 >= y1_r1 and y1_r2 <=y2_r1) or (y2_r2 >= y1_r1 and y2_r2 <=y2_r1):
			return True

	return False