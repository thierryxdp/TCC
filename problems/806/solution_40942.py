#Start your python function here
def colisao(ret1,ret2):
     """Função que dado duas tuplas com quatro valores inteiros cada, representando retângulos com as coordenadas de 'ret1' e as coordenadas do 'ret2', e retorna o valor booleano True caso haja interseção ou False, caso não haja; tupla,tupla -> bool."""
    x_inf_esq1,y_inf_esq1,x_sup_dir1,y_sup_dir1 = ret1
    x_inf_esq2,y_inf_esq2,x_sup_dir2,y_sup_dir2 = ret2

    return not(x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not(y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2)