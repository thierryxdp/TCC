def eh_quadrada(matriz):
    """Dada uma matriz retorna um valor booleano
    se essa matriz é uma matriz quadrada."""
    linhas = len(matriz)
    colunas = len(matriz)
    if linhas == colunas:
        return True
    else:
        return False