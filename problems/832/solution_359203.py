def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matriz)
    for i in range(linhas):
        colunas = len(matriz[0])
        for j in range(colunas):
            if linhas == colunas and linhas > 0:
                return True
            elif linhas == 0:
                return True
            else:
                return False