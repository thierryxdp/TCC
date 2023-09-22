#Start your python function here
def colisao(ret1,ret2):
    '''a função colisão recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vértices inferior esquerdo e superior direito do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se há colisão entre os 2 retângulos e False, caso contrário.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    return not (x_sup_dir2< x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2< y_inf_esq1 or y_sup_dir1 < y_inf_esq2)