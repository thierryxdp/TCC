def eh_quadrada(matriz):
    '''Função que recebe uma matriz e retorna um valor booleano
    indicando se ela é quadrada ou não
    list -> bool'''
    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])
    if numero_linhas == 0:
        return True
    elif numero_linhas == numero_colunas:
        return True
    else:
        return False