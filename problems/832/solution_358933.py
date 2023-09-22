def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    n_linhas = len(matriz)
    for n_linhas == 0:
        n_colunas == 0
        return True
    for i in range(n_linhas):
        n_colunas = len(matriz[0])
        if n_linhas == n_colunas:
            return True
        else:
            return False