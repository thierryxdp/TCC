def eh_quadrada(matriz):
    '''Função que recebe uma matriz e retorna um booleano que depende se o número 
    de linhas (len(matriz)) é igual ao número de colunas len(matriz[0])'''
    '''list --> bool'''
    x = len(matriz)
    if x > 0:
    	y = len(matriz[0])
    else:
        y = 0
    if x == y:
            return True
    else:
            return False