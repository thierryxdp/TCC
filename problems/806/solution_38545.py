#Start your python function here
def colisao(ret1,ret2):
    ret1v1x = ret1[0]
    ret1v1y = ret1[1]
    ret1v2x = ret1[2]
    ret1v2y = ret1[3]
    ret2v1x = ret2[0]
    ret2v2x = ret2[1]
    ret2v1y = ret2[2]
    ret2v2y = ret2[3]
    if ((ret1vix < ret2v1x and ret1v2y < ret2v1y and ret1v2x < ret2v2x and ret1v2y < ret2v2y) or (ret1v1x > ret2v1x and ret1v1y > ret2v1y and ret1v2x > ret2v2x and ret1v2y > ret2v2y)):
        return False
    else:
        return True
    
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado