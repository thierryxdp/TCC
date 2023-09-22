def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matriz)
    for i in range(linhas):
        if linhas == 0:
            colunas == 0
            return True
        for j in range(colunas):
            colunas = len(matriz[0])
            if linhas == colunas and linhas > 0:
                return True
            else:
                return False