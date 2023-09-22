def colisao(t_ret1,t_ret2):
    '''A funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    
    t_ret1 = (x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1)
    t_ret2 = (x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2)
    
    return return not((x_sup_dir1 < x_inf_esq2 or x_sup_dir2 < x_inf_esq1) or (y_sup_dir1 < y_inf_esq2 or y_sup_dir2 < y_inf_esq1))