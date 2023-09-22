def eh_quadrada(matriz):
    '''Função que retorna true se a matriz for quadrada e false caso contrário, dado a matriz;list->bool'''
    numero_de_linhas=len(matriz)
    if numero_de_linhas==0:
        return True
    numero_de_colunas=len(matriz[0])
    if numero_de_linhas==numero_de_colunas:
        return True
    else:
        return False