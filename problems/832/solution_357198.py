eh_quadrada(m):
    linhas = len(m)
    colunas = len(m[0])
    
    if linhas == colunas:
        return True
    elif linhas == 0 or colunas == 0:
        return True
    else:
        return False