def eh_quadrada(m):
    linhas = len(m)
    colunas = len(m[0])
    vazia = [[]]
    if linhas == colunas:
        return True
    if linhas != colunas:
        return False