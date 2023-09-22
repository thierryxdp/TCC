#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    a1 =  x_inf_esq1
    b1 =  y_inf_esq1
    c1 =  x_sup_dir1
    d1 =  y_sup_dir1
    a2 =  x_inf_esq2
    b2 =  y_inf_esq2
    c2 =  x_sup_dir2
    d2 =  y_sup_dir2
    ret1 = (a1 + (abs (a1) - abs (c1) * b1 + (abs (b1) - abs (d1))))
    ret2 = (a2 + (abs (a2) - abs (c2) * b2 + (abs (b2) - abs (d2))))
    if ret1 - ret2 != ret1 + ret2:
        return True
    else:
        return False