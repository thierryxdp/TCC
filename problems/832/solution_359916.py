def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == 0 :
        return True
    if linhas == colunas:
        return True