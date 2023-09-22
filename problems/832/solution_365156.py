def eh_quadrada(matriz):
    """Identifica se uma matriz e quadrade ou seja tenha
    mesmo numero de linhas e colunas;
    list[???][???] --> bool"""
    tamanho_l = len(matriz)

    for linhas in matriz:
        if (len(linhas) != tamanho_l):
            return False

    return True