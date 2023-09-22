def eh_quadrada(matrix):
    '''função booleana que determina se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matrix)
    colunas = 0
    for i in range(linhas):
    	if linhas == 0:
            colunas += 0
            return True
        if linhas > 0:
            if linhas == len(matriz[0]):
                return True
            elif linhas != len(matriz[0]):
                return False