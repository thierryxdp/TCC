def colisao(ret1,ret2):
    '''Funcao que recebe duas tuplas (com 4 valores int),
     representando as coordenadas do primeiro retângulo 
     e do segundo retângulo, e devolve True se ha colisão 
     entre os 2 retangulos e False, caso não haja colisão;
     tuple, tuple --> bool'''

    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    if not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2):
        return True
    else: 
        return False