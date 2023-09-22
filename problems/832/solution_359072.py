def eh_quadrada(matrix):
    '''função booleana que determina se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matrix)
    colunas = 0
    for i in range(linhas):
        if linhas >= 0:
            if linhas == len(matrix[0]):
                return True
            else:
                return False