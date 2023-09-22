#Start your python function here
def colisao(ret1,ret2):
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if x_inf_esq1==x_inf_esq2:
        return True
    if x_sup_dir1==x_sup_dir2:
        return True
    if y_inf_esq1==y_inf_esq2:
        return True
    if y_sup_dir1==y_sup_dir2:
        return True