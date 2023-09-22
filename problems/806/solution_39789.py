def calculo_colisao (ret1,ret2):
    if x_inf_esq2>= x_inf_esq1 and x_inf_esq2 <= x_sup_dir1:
        if y_inf_esq2 >= y_inf_esq1 and y_inf_esq2 <= y_sup_dir1:
            return True
    elif x_sup_dir2>= x_inf_esq1 and x_sup_dir2 <= x_sup_dir1:
            if y_sup_dir2 >= y_inf_esq1 and y_sup_dir2 <= y_sup_dir1:
                return True
    elif  x_inf_esq2>= x_inf_esq1 and  x_inf_esq2 <=  x_sup_dir1:
            if y_sup_dir2 >=  y_inf_esq1 and y_sup_dir2 <= y_sup_dir1:
                return True
    elif x_sup_dir2>= x_inf_esq1,and x_sup_dir2 <= x_sup_dir1:
            if y_inf_esq2 >= y_inf_esq1 and y_inf_esq2 <= y_sup_dir1:
                return True
    else:
        return False