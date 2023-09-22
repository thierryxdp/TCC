def colisao(ret1, ret2):
    '''A Função colisão recebe duas (2) tuplas com quatro valores inteiros
    coordenadas dos vertices inferior esquerdo e superior esquerdo do
    retangulo, nessa ordem, e devolve True se ha colisao entre as duas.
    tuple, tuples'''
    x_inf_esq1,
    y_inf_esq1,
    x_sup_dir1,
    y_sup_dir1 
    x_inf_esq2,
    y_inf_esq2,
    x_sup_dir2,
    y_sup_dir2 

    objeto1 = [x_inf_esq1, x_sup_dir1, x_inf_esq2, x_sup_dir2] == ret1
    objeto2 = [y_inf_esq1, y_sup_dir1, y_inf_esq2, x_sup_dir2] == ret2

    for objeto1 in objeto2:
        return True
    else:
        return False