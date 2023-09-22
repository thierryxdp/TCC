#Start your python function here
def colisao(ret1,ret2):
    '''a função colisão recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vértices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    JJie1 = x_inf_esq1
    KKie1 = y_inf_esq1
    JJsd1 = x_sup_dir1
    KKsd1 = y_sup_dir1
    JJie2 = x_inf_esq2
    KKie2 = y_inf_esq2
    JJsd2 = x_sup_dir2
    KKsd2 = y_sup_dir2

# segunda etapa - calculo do resultado
if ((JJie2<KKsd1) or (JJie1<JJsd2)) or ((KKie2<KKsd2) or (KKie2<JJsd2)):
    return 'False'
else:
    return 'True'