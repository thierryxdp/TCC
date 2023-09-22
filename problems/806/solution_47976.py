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
def colisao(retangulo_a, retangulo_b):
    x_esq_entre = retangulo_a[0] <= retangulo_b[0] <= retangulo_a[2]
    x_dir_entre = retangulo_a[0] <= retangulo_b[2] <= retangulo_a[2]

    y_inf_entre = retangulo_a[1] <= retangulo_b[1] <= retangulo_a[3]
    y_sup_entre = retangulo_a[1] <= retangulo_b[3] <= retangulo_a[3]

    if (x_esq_entre and y_inf_entre) or (x_esq_entre and y_sup_entre) or (x_dir_entre and y_inf_entre) or (x_dir_entre and y_sup_entre):
        return True
    else:
        return False