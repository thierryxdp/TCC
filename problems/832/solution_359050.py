def eh_quadrada(matrix):
    '''função booleana que determina se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matrix)
    for linhas in range(linhas):
        colunas = len(matrix[0])
        for j in range(colunas):
            if linhas == colunas:
                return True
            else:
                return False