#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    r1v1x = r1[0]
    r1v1y = r1[1]
    r1v2x = r1[2]
    r1v2y = r1[3]
    r2v1x = r2[0]
    r2v1y = r2[1]
    r2v2x = r2[2]
    r2v2y = r2[3]
    if ((r1v1x < r2v1x and r1v2y < r2v1y and r1v2x < r2v2x and r1v2y < r2v2y)) or ((r1v1x > r2v1x and r1v1y > r2v1y and r1v2x > r2v2x and r1v2y > r2v2y)):
        return False
    else:
        return True


# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado