def eh_quadrada(matriz):
    if len(matriz)== 0:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == colunas:
        return True
    
    else:
        return False