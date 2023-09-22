#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
	a_sup_dir_x=ret1[2]
	b_inf_esq_x=ret2[0]
	a_sup_dir_y=ret1[3]
	b_inf_esq_y=ret2[1]
	b_sup_dir_x=ret2[2]
	a_inf_esq_x=ret1[0]
	b_sup_dir_y=ret2[3]
	a_inf_esq_y=ret1[1]
	if (a_sup_dir_x < b_inf_esq_x or a_sup_dir_y < b_inf_esq_y or b_sup_dir_x < a_inf_esq_x or b_sup_dir_y < a_inf_esq_y ):
		return False
	else:
		return True