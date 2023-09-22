def eh_quadrada(matriz):
    '''
    Funcao que tem como entrada uma matriz e retorna True
    se a matriz for quadrada e False se não for quadrada.
    	Parametros:
        	entrada:
           		matriz : list
            saida:
            	bool
    '''
    n_linhas = len(matriz)
    if n_linhas == 0:
        return True
    n_colunas = len(matriz[0])
    if n_linhas == n_colunas:
        return True
    else:
        return False