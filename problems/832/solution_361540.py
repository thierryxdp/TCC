def eh_quadrada(matriz):
    """retorna se a matriz dada é quadrada ou nao"""
    """list -> bool"""
    linhas = len(matriz)
    if linhas == 0:
        return True
    else:
        colunas = len(matriz[0])
        if linhas == colunas:
            return True
        else:
            return False