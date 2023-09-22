def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    n_linhas = len(matriz)
    while n_linhas == 0:
        n_colunas == 0
        return True
    while i in range(n_linhas):
        n_colunas = len(matriz[0])
        while j in range(n_colunas):
            if n_colunas == n_linhas:
                return True
            elif n_colunas != n_linhas:
                return False