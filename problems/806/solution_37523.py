def colisao(retangulo1, retangulo2):
    """
    A função 'colisao' recebe duas tuplas com quatro valores inteiros cada uma, representando as 
    coordenadas dos vértices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
    retângulo, nessa ordem.
    tuple, tuple --> bool

    
    Returns:
    Devolve True se há colisao entre os 2 retângulos e False, caso contrário.
    """

    """
    # 1ª Etapa: extrair as coordenadas das tuplas recebidas como argumentos: """
    x_inf_esq1 = (retangulo1[0:1])
    y_inf_esq1 = (retangulo1[1:2])
    x_sup_dir1 = (retangulo1[2:3])
    y_sup_dir1 = (retangulo1[3:4])

    x_inf_esq2 = (retangulo2[0:1])
    y_inf_esq2 = (retangulo2[1:2])
    x_sup_dir2 = (retangulo2[2:3])
    y_sup_dir2 = (retangulo2[3:4])
    
    retangulo1 = [x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1]
    retangulo2 = [x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2]
   
    """
    # 2ª Etapa: Cálculo da colisão:  """   

   
    if (x_sup_dir1 < x_inf_esq2) or (x_sup_dir2 < x_inf_esq1) or (y_sup_dir1 < y_inf_esq2) or (y_sup_dir2 < y_inf_esq1):
        return False
    else:
        return True