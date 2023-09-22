def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matriz)
    for i in range(linhas):
        if not i in range(linhas):
            return true
        colunas = len(matriz[0])
        for j in range(colunas):
        	if linhas == colunas:
                return True
            else:
                return False