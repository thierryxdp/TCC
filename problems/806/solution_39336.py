def teste(pont, ret):
	"""função que verifica se um ponto esta dentro de um retangulo"""
	x_inf_esq, y_inf_esq, x_sup_dir, y_sup_dir = ret
	return x_inf_esq <= pont[0] and pont[0] <= x_sup_dir and y_inf_esq <= pont[1] and pont[1] <= y_sup_dir

def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
	x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
	return teste((x_inf_esq1, y_inf_esq1), ret2) or teste((x_sup_dir1, y_sup_dir1), ret2)