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
    n_colunas = len(matriz[0])
    if n_linhas == n_colunas:
        return True
    elif n_linhas == 0:
        n_colunas += []
        return True
    elif n_linhas != n_colunas:
        return False
       	#elif n_linhas == 0 and n_colunas == 0:
         #   return True