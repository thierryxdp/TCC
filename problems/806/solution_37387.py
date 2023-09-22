def colisao(ret1,ret2):
    '''Função que recebe duas tuplas com quatro valores inteiros cada, correspondentes 
    as coordenadas do vértices x e y, superior e interior, esquerdo e direito de cada retângulo e
    retorna True caso haja colisão e False caso não haja colisão.
    Entrada: tuple
    Saída: Bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if ret1==ret2:
    	return 'True'
    elif x_inf_esq1==x_inf_esq2 and y_inf_esq1>y_inf_esq2 and x_sup_dir1>x_sup_dir2 and y_inf_esq1>y_inf_esq2:
    	return 'True'
    elif x_inf_esq1<x_inf_esq2 and y_inf_esq1>y_inf_esq2 and x_sup_dir1<x_sup_dir2 and y_inf_esq1<y_inf_esq2:
    	return 'True'
    elif x_inf_esq1<x_inf_esq2 and y_inf_esq1<y_inf_esq2 and x_sup_dir1==x_sup_dir2 and y_inf_esq1<y_inf_esq2:
    	return 'True'
    else:
   		return 'False'