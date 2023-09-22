#Start your python function here
def colisao(ret1,ret2):
    if ret2[2]>=ret1[0] and ret2[3]>=ret1[1]:
        return True
    else:
        return False

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado