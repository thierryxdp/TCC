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
    if (x_inf_esq1>=x_inf_esq2 and x_inf_esq1<=x_sup_dir2) and (y_inf_esq1>=y_inf_esq2 and y_inf_esq1<=y_sup_dir2):
        return True
    elif (x_sup_dir1>=x_inf_esq2 and x_sup_dir1<=x_sup_dir2) and (y_inf_esq1>=y_inf_esq2 and y_inf_esq1<=y_sup_dir2):
        return True
    elif (x_inf_esq2>=x_inf_esq1 and x_inf_esq2<=x_sup_dir1) and (y_inf_esq2>=y_inf_esq1 and y_inf_esq2<=y_sup_dir1):
        return True
    elif (x_sup_dir2>=x_inf_esq1 and x_sup_dir2<=x_sup_dir1) and (y_inf_esq2>=y_inf_esq1 and y_inf_esq2<=y_sup_dir1):
        return True
    elif (y_sup_dir1>=y_inf_esq2 and y_sup_dir1<=y_sup_dir2) and (x_sup_dir1>=x_inf_esq2 and x_sup_dir1<=x_sup_dir2):
        return True
    elif (y_inf_esq1>=y_inf_esq2 and y_inf_esq1<=y_sup_dir2) and (x_sup_dir1>=x_inf_esq2 and x_sup_dir1<=x_sup_dir2):
        return True
    elif (y_sup_dir2>=y_inf_esq1 and y_sup_dir2<=y_sup_dir1) and (x_sup_dir2>=x_inf_esq1 and x_sup_dir2<=x_sup_dir1):
        return True
    elif (y_inf_esq2>=y_inf_esq1 and y_inf_esq2<=y_sup_dir1) and (x_sup_dir2>=x_inf_esq1 and x_sup_dir2<=x_sup_dir1):
        return True
    else:
        return False