def colisao(retangulo1,retangulo2):
    """ Função que, dados dois retângulos, verifica se eles colidiram, ou seja, se a interseção entre eles é diferente de vazio.
    Os lados de cada um dos retângulos s˜ao sempre paralelos aos eixos x e y.
    tupla, tupla -> bool. """
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = retangulo1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = retangulo2
    
    if y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2:
        return "False"
    if x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2:
        return "False"
    else:
        return "True"