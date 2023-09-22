def eh_quadrada(matriz):
    '''
    	Funcao que recebe uma matriz e identifica se e 
        quadrada
        list -> bool
    '''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    if qtd_linhas == qtd_colunas:
        return True
    elif qtd_linhas and qtd_colunas = 0:
        return True
    else:
        return False