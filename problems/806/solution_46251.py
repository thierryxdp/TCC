def colisao(ret1, ret2):
    """A função retorna se dois retângulos colidiriam ou não,
    dadas coordenadas dos pontos inferior direito e superior
    esquerdo de cada retângulo
    tupla, tupla -> booleano"""
    # primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    if x_inf_esq2 <= x_sup_dir1 and y_inf_esq2 <= y_sup_dir1:
        return True
    else:
        return False