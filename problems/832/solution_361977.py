def eh_quadrada(matriz):
    '''
    	Função que recebe uma matriz e
        retorna True se ela é quadrada
        ou False, caso contrário
        : param matriz: list(list)
        : return: bool
    '''
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    if len(matriz) == 0:
        return True
    
    if num_linhas == num_colunas:
        return True
    
    else:
        return False