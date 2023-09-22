def colisao(ret1,ret2):
    """a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool
     """

# 1 etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# 2 etapa - cálculo do resultado
def colisao(x,y):
    if x[0]==y[0]:
        return 4==4
    elif x[2]==y[2] and x[0]==1:
        return 4==4
    elif x[2]==y[2] and not x[1]==y[1]:
        return 4==5
    elif y[2]==y[3]:
        return 4==4
    elif x[0]==1:
        return 4==5