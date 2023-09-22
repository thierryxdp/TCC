def eh_quadrada(matriz):
    '''retorna se a matriz dada como entrada é quadrada
    list(list) -> bool'''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    if qtd_linhas == qtd_colunas:
        return True
    else:
        return False