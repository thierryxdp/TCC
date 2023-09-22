def colisao(ret1,ret2):
    x_inf_esq1 = ret1[:1]
    y_inf_esq1 = ret1[2:3]
    x_sup_dir1 = ret1[4:5]
    y_sup_dir1 = ret1[6:7]

    x_inf_esq2 = ret2[:1]
    y_inf_esq2 = ret2[2:3]
    x_sup_dir2 = ret2[4:5]
    y_sup_dir2 = ret2[6:7]

    #x->x_inf_esq1.  y->y_inf_esq1. width->x_sup_dir1. height y_sup_dir1
    #rect1 = {x: 5, y: 5, width: 50, height: 50}
    # x->x_inf_esq2.  y->y_inf_esq2. width->x_sup_dir2. height y_sup_dir2
    #rect2 = {x: 20, y: 10, width: 10, height: 10}



    if (x_inf_esq1 < x_inf_esq2 + x_sup_dir2 and
       x_inf_esq1 + x_sup_dir1 > x_inf_esq2 and
       y_inf_esq1 < y_inf_esq2 + x_sup_dir2 and
       y_inf_esq1 + y_sup_dir1 > y_sup_dir2):

        return True

    else:

        return False