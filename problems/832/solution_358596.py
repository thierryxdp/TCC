def eh_quadrada(matriz):
    '''função booleana que diz se uma matriz de entrada é
    quadrada ou não'''
    n_linhas = len(matriz)
    for i in range(n_linhas):
        n_colunas = len(matriz[0])
        for j in range(n_colunas):
            if n_linhas == n_colunas:
                return True
            elif n_linhas == 0:
                n_colunas == 0 
                return True 
            else:
                return False