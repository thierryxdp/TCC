def eh_quadrada(m:list):
    linhas = len(m)
    colunas = len(m[0])
    vazia = [[]]
 
    if linhas == colunas:
        return True
    if linhas != colunas:
        return False
    if m==vazia:
        return True
    else:
        return False