def eh_quadrada(m):
    if m == []:
        return False
    
    linhas = len(m)
    colunas = len(m[0])
    
    if linhas  == colunas:
        return True
    else:
        return False