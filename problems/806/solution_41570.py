def colisao(ret1,ret2):
    """ Dado a posição x1,y1,x2,y2 e x3,y3,x4,y4 vamos retornar se esses estão
        se cruzando.
        entrada -->int
        saida   -->int """
    x_inf_esq1(x1), y_inf_esq1(y1), x_sup_dir1(x2), y_sup_dir1(y2) = ret1
    x_inf_esq2(x3), y_inf_esq2(y3),  x_sup_dir2(x4), y_sup_dir2(y4) = ret2
    if (x_sup_dir1<x_inf_esq2)or(x_sup_dir2<x_inf_esq1)or(y_sup_dir1<y_inf_esq2)or(y_sup_dir2<y_inf_esq1):
        return False
    else:
        return True