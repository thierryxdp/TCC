def eh_quadrada(matriz):
    """Define se uma matriz é quadrdada ou não
    list -> bool"""
    if str(matriz) =="[]" :
        return True
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    if linhas != colunas:
        return False