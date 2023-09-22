def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == colunas:
       	return True
    if matriz == []:
        return True
    else:
        return False