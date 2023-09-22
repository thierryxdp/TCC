#Start your python function here
def colisao(ret1,ret2):
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2     
    if int(x_sup_dir1) < int(x_inf_esq2) or int(x_sup_dir2) < int(x_inf_esq1) or int(y_sup_dir1) < int(y_inf_esq2) or int(y_sup_dir2)  int(x_sup_dir2) or int(x_inf_esq2) > int(x_sup_dir1) or int(y_inf_esq1) > int(y_sup_dir2) or int(y_inf_esq2) > int(y_sup_dir1):
        return('True')