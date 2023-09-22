def colisao(ret1, ret2):
    '''A Função colisão recebe duas (2) tuplas com quatro valores inteiros
    coordenadas dos vertices inferior esquerdo e superior esquerdo do
    retangulo, nessa ordem, e devolve True se ha colisao entre as duas.
    tuple, tuple ---> bool '''

    #    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    #    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    a=ret1[0]*ret2[0]*ret1[2]*ret2[2]%4
    b=ret1[1]*ret2[1]*ret1[3]*ret2[3]%4
    
    if a < b :
        return True
    if a > b  :
        return False
    else :
        return 'Programando'