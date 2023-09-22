def colisao(ret1,ret2):
    """recebe duas tuplas com quatro valores int cada;
representa as coordenadas dos vertices inf esquerdo e
sup esquerdo do primeiro retângulo e do segundo retângulo,
nessa ordem; devolve True se tiver colisao entre os 2 retangulos e False,
caso contrario.   |   tuple, tuple --> bool"""
#igualando os argumentos às coordenadas
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x1, y1, x2, y2 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    x3, y3, x4, y4 = ret2 
#verifica se houve colisão   
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return False
    else:
        return True