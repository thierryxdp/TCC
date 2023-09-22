def eh_quadrada(matriz):
    """Função"""
    if matriz==[]:
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas!=colunas:
        return False
    else:
        return True