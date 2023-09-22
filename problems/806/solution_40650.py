def colisao(quad1,quad2):
    '''skfndknfd'''
    quad1 = x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    quad2 = x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2
    if(x_sup_dir1<x_inf_esq2 or x_sup_dir2 < x_inf_esq1) or (y_sup_dir1 < y_inf_esq2 or y_sup_dir2 < y_inf_esq1):
        return False
    else:
        return True