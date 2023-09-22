#Start your python function here
def colisao(ret1,ret2):
    if colisao(0)>colisao(6) or colisao(2)<colisao(4) or colisao(1)>colisao(7) or colisao(3)<colisao(5):
        return "False"
    else:
        return "True"
   


    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2