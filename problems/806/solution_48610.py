def colisao(ret1, ret2):
    '''A Função colisão recebe duas (2) tuplas com quatro valores inteiros
    coordenadas dos vertices inferior esquerdo e superior esquerdo do
    retangulo, nessa ordem, e devolve True se ha colisao entre as duas.
    tuple, tuples'''


    ret1 =[]
    ret1 = info1
    ret2 =[]
    ret2 = info2 
    info1 = [x_inf_esq1, x_sup_dir1, x_inf_esq2, x_sup_dir]
    info1 = [x_inf_esq1 * x_sup_dir1 * x_inf_esq2 * x_sup_dir]    
    x = info1
    info2 = [y_inf_esq1, y_sup_dir1, y_inf_esq2, x_sup_dir2]
    info2 = [y_inf_esq1 * y_sup_dir1 * y_inf_esq2 * x_sup_dir2]
    y = info2
        
    if x < y:

        return True
    else:
        return False