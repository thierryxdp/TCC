#Start your python function here
def colisao(ret1,ret2):
    '''a função colisão recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vértices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    Jie1 = x_inf_esq1
    Kie1 = y_inf_esq1
    Jsd1 = x_sup_dir1
    Ksd1 = y_sup_dir1
    Jie2 = x_inf_esq2
    Kie2 = y_inf_esq2
    Jsd2 = x_sup_dir2
    Ksd2 = y_sup_dir2

# segunda etapa - calculo do resultado
    if ((Jsd1<Jie2) or (Jsd2<Jie1)) or ((Ksd1<Kie2) or (Ksd2<Kie1)):    
        return 'False'
    else:
         return 'True'