def eh_quadrada(matriz):
    '''função que recebe uma matriz e verifica se ela é quadrada.
    list -> bool'''
    i=0
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    if linhas==0 and colunas==0:
        return True
    else:
        return False