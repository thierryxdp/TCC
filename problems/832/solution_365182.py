def eh_quadrada(matriz):
    """Calcula e retorna se a matriz eh quadrada, sem nenhuma linha, nem coluna; list--> bool"""
    linhas=len(matriz)
    for j in matriz:
            if len(j) != linhas :
                return False
    return True