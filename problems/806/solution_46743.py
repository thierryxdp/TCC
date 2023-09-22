def colisao(ret1,ret2):
    
    # primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2
    
    # segunda etapa - calculo do resultado
    # se o extremo mais a direita de um retangulo esta antes do
    # extremo mais a esquerda do outro nao tem como ter batida
    if x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2:
        return False
    
    # se o extremo mais acima de um retangulo esta abaixo do
    # extremo mais abaixo do outro nao tem como ter batida
    if y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2:
        return False

    # se chegou aqui eh porque tem batida
    return True

# segunda etapa - calculo do resultado