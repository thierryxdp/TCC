def colisao(ret1,ret2):
    '''A função colisão recebe duas tuplas com quatro valores inteiros cada uma, 
    representando as coordenadas dos vértices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, 
    e devolve True se há colisão entre os 2 retângulos e False, caso contrario;
    tuple, tuple --> bool'''
     
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
    return not(x_inf_esq2>x_sup_dir1 or x_inf_esq1>x_sup_dir2) and not (y_inf_esq2>y_sup_dir1 or y_inf_esq1>y_sup_dir2)