#Start your python function here
def colisao(ret1,ret2):
    """ a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
        
        Parameters:
            ret1 = tupla com quatro valores referentes as coordenadas dos pontos inferior esquerdo e superior direito do primeiro retangulo (x do canto inferior esquerdo, y do canto inferior esquerdo, x do canto superior direito, y do canto superior direito)
            ret2 = tupla com quatro valores referentes as coordenadas dos pontos inferior esquerdo e superior direito do primeiro retangulo (x do canto inferior esquerdo, y do canto inferior esquerdo, x do canto superior direito, y do canto superior direito)
        
        Testes:
            filtra_pares((1,2,3,4)) = (2,4)
            filtra_pares((2,4,6,8)) = (2,4,6,8)
            filtra_pares((1,3,5,7)) = ()

        Returns:
            True se ha colisao entre os 2 retangulos e False, caso contrario.
            tuple, tuple --> bool
    """
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2

    diagonal1 = ((x_sup_dir1 - x_inf_esq1)**2 + (y_sup_dir1 - y_inf_esq1)**2)**(1/2)
    diagonal2 = ((x_sup_dir2 - x_inf_esq2)**2 + (y_sup_dir2 - y_inf_esq2)**2)**(1/2)
    reta_sup1_sup2 = ((x_sup_dir1 - x_sup_dir2)**2 + (y_sup_dir1 - y_sup_dir2)**2)**(1/2)
    reta_sup1_inf2 = ((x_sup_dir1 - x_inf_esq2)**2 + (y_sup_dir1 - y_inf_esq2)**2)**(1/2)
    reta_inf1_sup2 = ((x_inf_esq1 - x_sup_dir2)**2 + (y_inf_esq1 - y_sup_dir2)**2)**(1/2)
    reta_inf1_inf2 = ((x_inf_esq1 - x_inf_esq2)**2 + (y_inf_esq1 - y_inf_esq2)**2)**(1/2)

    if reta_inf1_inf2 <= diagonal1 or reta_inf1_inf2 <= diagonal2:
        return True
    else:
        return False