def colisao(ret1, ret2):
    '''A Função colisão recebe duas (2) tuplas com quatro valores inteiros
    coordenadas dos vertices inferior esquerdo e superior esquerdo do
    retangulo, nessa ordem, e devolve True se ha colisao entre as duas.
    tuple, tuples'''


    ret1 =[]
    ret1 =(x_inf_esq1, x_sup_dir1, x_inf_esq2, x_sup_dir2)
    ret2 =[]
    ret2 = (y_inf_esq1, y_sup_dir1, y_inf_esq2, x_sup_dir2) 

    ret1[0]=x_inf_esq1
    ret1[1]=x_sup_dir1
    ret1[2]=x_inf_esq2
    ret1[3]=x_sup_dir

    ret2[0]=y_inf_esq1
    ret2[1]=y_sup_dir1
    ret2[2]=y_inf_esq2
    ret2[3]=x_sup_dir2
    
    if ret1[0] in ret1 or ret2:

        return True
    else:
        return False