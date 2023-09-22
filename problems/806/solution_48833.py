def colisao( x_sup_dir1, x_inf_esq2, y_sup_dir2, y_inf_esq1,y_sup_dir1 ,y_inf_esq2, x_sup_dir2, x_inf_esq1):
    '''dado dos retângulos, determinado pelas coordenadas x e y  de dois de seus vérticies diametralmente opostos, representando a diagonal que vai da esquerda para  a direita e de baixo para cima. Os lado são paralelos ao eixo x e y diagonal que vai da esquerda para a direita e de baixo pra cima;
    float,float,float,float,float,float,float,float->bool'''
    if not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2):
        return True
    else:
        return False