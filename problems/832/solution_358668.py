def eh_quadrada(matriz):
    '''função booleana que afirma se uma matriz é quadrada
    ou não; list -> bool'''
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            if n_colunas == n_linhas and n_colunas > 0:
                return True
            if n_colunas == 0:
                return True
            else:
                return False