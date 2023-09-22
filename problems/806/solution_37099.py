#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    a1 = x_inf_esq1, y_inf_esq1
    a2 = x_sup_dir1, y_inf_esq1
    a3 = x_sup_dir1, y_sup_dir1
    a4 = x_inf_esq1, y_sup_dir1

    b1 = x_inf_esq2, y_inf_esq2
    b2 = x_sup_dir2, y_inf_esq2
    b3 = x_sup_dir2, y_sup_dir2
    b4 = x_inf_esq2, y_sup_dir2

# segunda etapa - calculo do resultado
    if a1 == b1 or a1 == b2 or a1 == b3 or a1 == b4:
        return True

    elif a2 == b1 or a2 == b2 or a2 == b3 or a2 == b4:
        return True

    elif a3 == b1 or a3 == b2 or a3 == b3 or a3 == b4:
        return True

    elif a4 == b1 or a4 == b2 or a4 == b3 or a4 == b4:
        return True

    else:
        return False