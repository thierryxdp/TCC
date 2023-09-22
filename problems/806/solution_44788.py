from math import *
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    Largura_1 = L1 = abs(x_inf_esq1-x_sup_dir1)
    Largura_2 = L2 = abs(x_inf_esq2-x_sup_dir2)
    Altura_1 = A1 = abs(y_inf_esq1-y_sup_dir1)
    Altura_2 = A2 = abs(y_inf_esq2-y_sup_dir2)

    if x_inf_esq1 > x_inf_esq2:
        L=L2
    else:
        L=L1
    if y_inf_esq1 > y_inf_esq2:
        A=A2
    else:
        A=A1

    if abs(x_inf_esq1-x_inf_esq2)>= L or abs(y_inf_esq1-y_inf_esq2)>= A:
        return True
    else:
        return False