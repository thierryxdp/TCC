def eh_quadrada(matriz: list) -> bool:
    """comentário"""
    linhas = 0
    colunas = 0
    if matriz == []:
        return False 
    for i in range(len(matriz)):
        linhas += 1
        for j in range(len(matriz[i])):
            colunas += 1
    if linhas == colunas:
        return True
    else:
        return False