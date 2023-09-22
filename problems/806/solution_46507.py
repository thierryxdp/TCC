#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
x_inf_esq=int(ret2[0])
	x_inf_dir=int(ret2[1])
	x_sup_esq=int(ret2[2])
	x_sup_dir=int(ret2[3])

	y_inf_esq=int(ret1[0])
	y_inf_dir=int(ret1[1])
	y_sup_esq=int(ret1[2])
	y_sup_dir=int(ret1[3])
	if x_sup_esq==y_inf_esq or x_sup_esq==y_inf_dir or x_sup_esq==y_sup_esq or x_sup_esq==y_sup_dir :
		return True
	elif x_sup_dir==y_sup_dir or x_sup_dir==y_inf_dir or x_sup_dir==y_sup_esq or x_sup_dir==y_inf_esq:
		return True
	elif x_inf_esq==y_sup_esq or x_inf_esq==y_inf_dir or x_inf_esq==y_sup_dir or x_inf_esq==y_inf_esq:
		return True
	elif x_inf_dir==y_sup_esq or x_inf_dir==y_inf_esq or x_inf_dir==y_sup_dir or x_inf_dir==y_inf_dir:
		return True
	else:
		return False