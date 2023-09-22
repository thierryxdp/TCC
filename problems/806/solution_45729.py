def colisao(ret1,ret2):
    '''Recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     Entrada: tuple, tuple 
     Saída: bool
     '''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xie1, yie1, xsd1, ysd1 = ret1
    xie2, yie2, xsd2, ysd2 = ret2

# segunda etapa - calculo do resultado
not (xsd2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2)