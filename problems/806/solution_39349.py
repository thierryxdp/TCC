#Start your python function here
def colisao(ret1x1,ret1y1,ret1x2,ret1y2,ret2x1,ret2y1,ret2x2,ret2y2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
	x1=ret1x1 <= ret2x1 <= ret1x2
    x2=ret1x1 <= ret2x2 <= ret1x2
    y1=ret1y1 <= ret2y1 <= ret1y2
    y2=ret1y1 <= ret2y2 <= ret1y2
    if (x2 and y1) or (x1 and y2) == True:
        return True
    else:
        return False