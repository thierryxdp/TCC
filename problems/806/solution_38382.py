#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultadodef colisao(ret1,ret2):
    rect1_x = ret1[:5]
    rect1_y = ret1[:5]
    rect1_width = ret1[:50]
    rect1_height = ret1[:50]

    rect2_x = ret2[:20]
    rect2_y = ret2[:10]
    rect2_width = ret2[:10]
    rect2_height = ret2[:10]

    if (ret1< ret2 + ret2 and
        ret1 + ret1 > ret2 and
        ret1 < ret2 + ret2 and
        ret1 + ret1 > ret2):
        return True