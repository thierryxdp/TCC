def colisao((x_sup_dir1,y_sup_dir1,x_inf_esq1,y_inf_esq1),(x_sup_dir2,y_sup_dir2,x_inf_esq2,y_inf_esq2)):
    """ """
    if (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2):
        return False
    else:
        return True