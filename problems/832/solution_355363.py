def eh_quadrada(matriz):
    '''identifica se a matriz é quadrada ou não;
    list(list) -> bool'''
    if matriz == []:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False