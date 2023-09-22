def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if linhas == colunas:
                return True
            else:
                return False