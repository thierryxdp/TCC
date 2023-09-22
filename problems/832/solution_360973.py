def eh_quadrada(m):
    linhas = len(m)
    colunas = len(m[0])
    if m == []:
        return True
    for i in range(linhas):
        if linhas == colunas:
            return True
    if linhas != colunas:
        return False