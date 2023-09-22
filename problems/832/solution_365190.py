def eh_quadrada(matriz):
    """Calcula e retorna se a matriz eh quadrada, sem nenhuma linha, nem coluna; list--> bool"""
    linhas=len(matriz)
    if linhas==0:
        return True
    colunas=len(matriz[0])
    elif linhas==colunas:
        return True
    else:
        return False