def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_esq1, y_inf1, x_dir1, y_sup1 = ret1
    x_esq2, y_inf2,  x_dir2, y_sup2 = ret2
    if ret1 == ret2:
        return True
    if x_esq1+x_dir1>x_dir2+x_esq2:
        return True
    if y_inf2+y_sup2>y_sup1+y_inf2:
        return True
    else:
        return False
# segunda etapa - calculo do resultado