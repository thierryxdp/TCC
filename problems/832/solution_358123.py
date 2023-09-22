def eh_quadrada(matriz):
    '''função que recebe uma matriz e verifica se ela é quadrada.
    list -> bool'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == colunas:
        return True
    elif linhas != colunas:
        return False
    elif linhas==0:
        return True