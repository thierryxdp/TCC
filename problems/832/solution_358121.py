def eh_quadrada(matriz):
    '''função que recebe uma matriz e verifica se ela é quadrada.
    list -> bool'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    elif linhas and colunas not in matriz:
        return True
    else:
        return False