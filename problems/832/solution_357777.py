def eh_quadrada(matriz):
    quantidade_linhas = len(matriz)
    quantidade_colunas = 0

    if quantidade_linhas > 0:
        for coluna in matriz[0]:
            quantidade_colunas += 1

    return quantidade_linhas == quantidade_colunas