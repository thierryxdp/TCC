#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    diagonal_inf_ret1 = (ret1[0:2])
    diagonal_sup_ret1 = (ret1[2:])
    diagonal_inf_ret2 = (ret2[0:2])
    diagonal_sup_ret2 = (ret2[2:])

# segunda etapa - calculo do resultado
	if diagonal_inf_ret1 == diagonal_sup_ret2 or diagonal_sup_ret1 == diagonal_inf_ret2:
        return True