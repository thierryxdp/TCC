def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    x1 = tupla2[0]
    x2 = tupla2[2]
    y1 = tupla2[1]
    y2 = tupla2[3]
    colisao = False
    if (tupla1[0] <= x1) and (tupla1[2] >= x1):
        colisao = True
    elif (tupla1[0] <= x2) and (tupla1[2] >= x2):
        colisao = True
    elif (tupla1[1] <= y1) and (tupla1[3] >= y1):
        colisao = True
    elif (tupla1[1] <= y1) and (tupla1[3] >= y1):
        colisao = True
    print(colisao)