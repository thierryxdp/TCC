def eh_quadrada(matriz):
    '''função booleana para ver se a matriz de entrada é 
    quadrada ou não. List -> bool'''
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            if n_linhas == n_colunas:
                return True
            elif n_linhas == 0:
                n_colunas == 0
                return True
            else:
                return False