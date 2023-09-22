def eh_quadrada(m:list):
    linhas = len(m)
    vazia = [[]]
    
    if linhas == len(m[0]):
        return True
    if linhas != len(m[0]):
        return False