def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
	if (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < X_inf_esq2):
        return true
        if (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2):
            return false