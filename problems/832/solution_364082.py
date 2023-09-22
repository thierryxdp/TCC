def eh_quadrada(matriz):
    '''Função que retorna true se a matriz for quadrada e false caso contrário, dado a matriz;list->bool'''
    numero_de_linhas=len(matriz)
    numero_de_colunas=len(matriz[0])
    return numero_de_linhas==numero_de_colunas