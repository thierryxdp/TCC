#Problema possui 2 retangulos e quer saber se eles colidem ou nao
#Para isso, usa-se 2 casos
#No 1 caso, o denominado ret1 esta à esquerda do ret2
#No 2 caso, o denonimado ret1 esta à direita do ret 2
#Achar que o valor x ou o valor y colida com o outro retangulo, ja satisfaz a situação

def colisao(ret1,ret2):
    """Funcao retorna a informacao se os retangulos colidiram ou não
    tupla, tupla - > booleano."""
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2
    if(x_sup_dir1<x_inf_esq2 or x_sup_dir2 < x_inf_esq1) or (y_sup_dir1 < y_inf_esq2 or y_sup_dir2 < y_inf_esq1):
        return False
    else:
        return True