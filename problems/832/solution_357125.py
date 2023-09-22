def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])-1
    if linhas == colunas:   
        return True
    elif colunas == 0:
        return True
    elif linhas == 0:
        return True
    else: 
        return False