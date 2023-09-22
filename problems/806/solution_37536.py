def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    a_inf_esq_x, a_inf_esq_y, a_sup_dir_x, a_sup_dir_y = ret1
    b_inf_esq_x, b_inf_esq_y,  b_sup_dir_x, b_sup_dir_y = ret2
    if (a_sup_dir_x < b_inf_esq_x) or (a_sup_dir_y < b_inf_esq_y) or (b_sup_dir_x < a_inf_esq_x) or (b_sup_dir_y < a_inf_esq_y):
        return False
    else:
        return True