#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
     if (int(x_inf_esq1)<=int(x_inf_esq2)<=int(x_sup_dir1)<=int(x_sup_dir2) or int(x_inf_esq1)<=int(x_inf_esq2)<=int(x_sup_dir2)<=int(x_sup_dir1)) and (int(y_inf_esq1)<=int(y_inf_esq2)<=int(y_sup_dir1)<=int(y_sup_dir2) or int(y_inf_esq1)<=int(y_inf_esq2)<=int(y_sup_dir2)<=int(y_sup_dir1)):
        return('true')
     if (int(x_inf_esq1)<int(x_sup_dir1)<int(x_inf_esq2)<int(x_sup_dir2)) and (int(y_inf_esq1)<int(y_sup_dir1)<int(y_inf_esq2)<int(y_sup_dir2)):
        return('false')
                                                                                                                                                                                                                                                                                                           
# segunda etapa - calculo do resultado