def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matriz)
    i = 0
    for i in range(linhas):
        for i in range(linhas):
            if linhas == 0:
                return True
            if linhas > 0:
                for i in range(linhas):
                    colunas = len(matriz[0])
                    for j in range(colunas):
                        if linhas == colunas:
                            return True
                        else:
                            return False