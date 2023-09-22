def eh_quadrada(matriz):
    if [] in matriz:
        return True
    if linhas == colunas:
        linhas = len(matriz)
        colunas = len(matriz[0])
        return True
    else: 
        return False