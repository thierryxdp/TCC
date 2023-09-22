def eh_quadrada(matriz):
    """ Função que verifica se a matriz dada é quadrada
    	(possui mesmo número de linhas e colunas)
    list -> bool"""
    for i in matriz:
        if len(matriz) != len(i):
            return False
    return True