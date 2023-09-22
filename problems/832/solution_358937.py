def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    n_linhas = len(matriz)
    for i in range(n_linhas):
        n_colunas = len(matriz[0])
        for j in range(n_colunas):
            if n_linhas == n_colunas:
                return True
            else:
                return False