#Start your python function here
def colisao(mat):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1 = int(mat[0][0])
    y_inf_esq1 = int(mat[0][1])
    x_sup_dir1 = int(mat[0][2])
    y_sup_dir1 = int(mat[0][3])
    
    x_inf_esq2 = int(mat[1][0])
    y_inf_esq2 = int(mat[1][1])
    x_sup_dir2 = int(mat[1][2])
    y_sup_dir2 = int(mat[1][3])

# segunda etapa - calculo do resultado
	return not(x_sup_dir1 < x_inf_esq2 or y_sup_dir1 < y_inf_esq2 or x_sup_dir2 < x_inf_esq1 or y_sup_dir2 < y_inf_esq1)