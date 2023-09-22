def colisao(ret1,ret2):
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if (y_inf_esq2 > y_sup_dir1 or y_inf_esq1 > y_sup_dir2 or x_sup_dir1 < x_inf_esq2 or x_sup_dir2 < x_inf_esq1):
      return False
    else:
      return True