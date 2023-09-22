def colisao(ret1,ret2):
    '''
    Detecta se há colisão entre doi retângulos.
    tuple, tuple --> bool
    '''
    x_inf_esq1=ret1[0]
    y_inf_esq1=ret1[1]
    x_sup_dir1=ret1[2]
    y_sup_dir1=ret1[3]
    x_inf_esq2=ret2[0]
    y_inf_esq2=ret2[1]
    x_sup_dir2=ret2[2]
    y_sup_dir2=ret2[3]
    if ((y_sup_dir1>=y_inf_esq1 and y_sup_dir1<=y_sup_dir2) or (x_inf_esq1>=x_inf_esq2 and x_inf_esq1<=x_sup_dir2)) or ((y_sup_dir2>=y_inf_esq1 and y_sup_dir2<=y_inf_esq1) or (x_inf_esq2>=x_inf_esq1 and x_inf_esq2<=x_sup_dir1)):
        return True
    else:
        return False