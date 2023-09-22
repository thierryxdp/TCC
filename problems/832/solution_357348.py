def eh_quadrada(matriz):
    '''Funcao que verifica se a
    matriz dada e quadrada ou nao.
    Dados de entrada: list[list]
    Valor de saida: bool
    '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    if matriz == []:
        return True 
    if linhas == colunas:
        return True
    else:
        return False