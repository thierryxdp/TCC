#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
	x1 = ret1 [0]
    y1 = ret1 [1]
    x2 = ret1 [2]
    y2 = ret1 [3]
    x3 = ret2 [0]
    y3 = ret2 [1]
    x4 = ret2 [2]
    y4 = ret2 [3]
	if (x1 >= x3) or (x2 >= x4)  or (y1 >= y3) or (y2 >= y4):
        return True
    elif (x3 <= x2) or (y3 <= y2):
        return True
    elif (y3 < y4):
        return False
    else:
        return False