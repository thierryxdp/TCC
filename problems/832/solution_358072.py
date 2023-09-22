def eh_quadrada(m):
    linhas = len(m)
    colunas = len(m[0])
    vazia = [[]]
    if len(m) == colunas:
        return True
    if len(m)!= colunas:
        return False