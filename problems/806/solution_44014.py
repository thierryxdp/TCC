#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq3, y_inf_esq4,  x_sup_dir3, y_sup_dir4 = ret2

# segunda etapa - calculo do resultado
    if (int(x_sup_dir1)<int(x_inf_esq3)) or (int(y_sup_dir2)<int(y_inf_esq4)) or (int(x_sup_dir3)<int(x_inf_esq1)) or (int(y_sup_dir4)<int(y_inf_esq2)):
        return 0==0
    else:
        return 1==0